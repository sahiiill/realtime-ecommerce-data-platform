import json
import random
import time
from datetime import datetime
from streaming.config import KAFKA_BROKER, KAFKA_TOPIC
from streaming.logger import setup_logger

import signal
import sys

from faker import Faker
from kafka import KafkaProducer
from jsonschema import validate, ValidationError
from streaming.schema import EVENT_SCHEMA

logger = setup_logger("logs/producer.log")
fake = Faker()


event_count = 0
start_time = time.time()

def shutdown_handler(signal_received, frame):

    logger.info("Shutdown signal received. Closing Kafka producer...")

    producer.flush()
    producer.close()

    logger.info("Kafka producer closed successfully.")

    sys.exit(0)
    
signal.signal(signal.SIGINT, shutdown_handler)



producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),

    linger_ms=10, 
    batch_size=16384,
    acks="all", 
    retries=5
)

EVENT_TYPES = [
    "page_view",
    "add_to_cart",
    "purchase"
]

PRODUCTS = [
    "iphone_15",
    "samsung_s24",
    "macbook_pro",
    "airpods_pro",
    "sony_wh1000xm5"
]


def generate_event():
    event_type = random.choice(EVENT_TYPES)

    return {
        "event_id": fake.uuid4(),
        "user_id": random.randint(1000, 9999),
        "event_type": event_type,
        "product_name": random.choice(PRODUCTS),
        "price": round(random.uniform(50, 2500), 2),
        "quantity": random.randint(1, 5),
        "event_timestamp": datetime.utcnow().isoformat(),
        "user_country": fake.country(),
        "device_type": random.choice(["mobile", "desktop", "tablet"])
    }


if __name__ == "__main__":
    logger.info("Starting ecommerce Kafka producer...")

    while True:
        event = generate_event()

        try:
            validate(instance=event, schema=EVENT_SCHEMA)

            producer.send(KAFKA_TOPIC, value=event)

            event_count += 1

            elapsed_time = time.time() - start_time
            events_per_second = round(event_count / elapsed_time, 2)

            logger.info(
                f"Produced valid event: {event['event_id']} | "
                f"Throughput: {events_per_second} events/sec"
            )

        except ValidationError as error:

            failed_path = "storage/failed/failed_events.jsonl"

            with open(failed_path, "a") as failed_file:
                failed_record = {
                    "event": event,
                    "error": str(error)
                }

                failed_file.write(json.dumps(failed_record) + "\n")

            logger.error(f"Schema validation failed: {error}")

        time.sleep(2)
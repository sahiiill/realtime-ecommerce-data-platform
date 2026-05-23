import json
import logging
import random
import time
from datetime import datetime

from faker import Faker
from kafka import KafkaProducer

fake = Faker()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

TOPIC_NAME = "ecommerce-events"

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
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

        producer.send(TOPIC_NAME, value=event)

        logger.info(f"Produced event: {event['event_id']}")

        time.sleep(2)
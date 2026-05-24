import json
import time
from datetime import datetime
from pathlib import Path
from streaming.config import KAFKA_BROKER, KAFKA_TOPIC
from streaming.logger import setup_logger

from kafka import KafkaConsumer

logger = setup_logger("logs/consumer.log")

event_count = 0
start_time = time.time()



consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="ecommerce-consumer-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

logger.info("Starting Kafka consumer...")


def get_output_path():
    current_date = datetime.utcnow().strftime("%Y-%m-%d")

    directory = Path(f"storage/raw/{current_date}")

    directory.mkdir(parents=True, exist_ok=True)

    return directory / "events.jsonl"


for message in consumer:
    event = message.value

    output_path = get_output_path()

    with open(output_path, "a") as file:
        file.write(json.dumps(event) + "\n")

    event_count += 1

    elapsed_time = time.time() - start_time
    events_per_second = round(event_count / elapsed_time, 2)

    logger.info(
        f"Stored event: "
        f"{event['event_id']} | "
        f"{event['event_type']} | "
        f"{event['product_name']} | "
        f"Throughput: {events_per_second} events/sec"
)
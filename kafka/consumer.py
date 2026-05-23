import json
import logging
from datetime import datetime
from pathlib import Path

from kafka import KafkaConsumer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

TOPIC_NAME = "ecommerce-events"

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers="localhost:9092",
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

    logger.info(
        f"Stored event: "
        f"{event['event_id']} | "
        f"{event['event_type']} | "
        f"{event['product_name']}"
    )
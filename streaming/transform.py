import json

from pathlib import Path


RAW_PATH = Path("storage/raw")
PROCESSED_PATH = Path("storage/processed")


def transform_events():

    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

    output_file = PROCESSED_PATH / "processed_events.jsonl"

    processed_count = 0

    with open(output_file, "w", encoding="utf-8") as processed:

        for raw_file in RAW_PATH.rglob("*.jsonl"):

            with open(raw_file, "r", encoding="utf-8") as source:

                for line in source:

                    event = json.loads(line)

                    transformed_event = {
                        "event_id": event["event_id"],
                        "user_id": event["user_id"],
                        "event_type": event["event_type"],
                        "product_name": event["product_name"],
                        "total_price": round(
                            event["price"] * event["quantity"], 2
                        ),
                        "user_country": event["user_country"],
                        "device_type": event["device_type"]
                    }

                    processed.write(
                        json.dumps(transformed_event) + "\n"
                    )

                    processed_count += 1

    print(f"Processed {processed_count} events")


if __name__ == "__main__":

    transform_events()
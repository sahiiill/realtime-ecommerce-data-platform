EVENT_SCHEMA = {
    "type": "object",
    "properties": {
        "event_id": {"type": "string"},
        "user_id": {"type": "integer"},
        "event_type": {"type": "string"},
        "product_name": {"type": "string"},
        "price": {"type": "number"},
        "quantity": {"type": "integer"},
        "event_timestamp": {"type": "string"},
        "user_country": {"type": "string"},
        "device_type": {"type": "string"}
    },
    "required": [
        "event_id",
        "user_id",
        "event_type",
        "product_name",
        "price",
        "quantity",
        "event_timestamp",
        "user_country",
        "device_type"
    ]
}
from jsonschema import validate, ValidationError

from streaming.schema import EVENT_SCHEMA


def test_valid_event():

    valid_event = {
        "event_id": "123",
        "user_id": 1001,
        "event_type": "purchase",
        "product_name": "iphone_15",
        "price": 999.99,
        "quantity": 1,
        "event_timestamp": "2026-05-23T10:00:00",
        "user_country": "Germany",
        "device_type": "mobile"
    }

    validate(instance=valid_event, schema=EVENT_SCHEMA)


def test_invalid_event():

    invalid_event = {
        "event_id": "123",
        "user_id": "INVALID_USER_ID",
        "event_type": "purchase",
        "product_name": "iphone_15",
        "price": 999.99,
        "quantity": 1,
        "event_timestamp": "2026-05-23T10:00:00",
        "user_country": "Germany",
        "device_type": "mobile"
    }

    try:
        validate(instance=invalid_event, schema=EVENT_SCHEMA)

        assert False

    except ValidationError:
        assert True
# schemas/user_schema.py

user_schema = {
    "type": "object",
    "required": ["id", "name", "username", "email", "address", "phone", "website", "company"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
        "address": {
            "type": "object",
            "properties": {
                "street": {"type": "string"},
                "suite": {"type": "string"},
                "city": {"type": "string"},
                "zipcode": {"type": "string"}
            }
        },
        "phone": {"type": "string"},
        "website": {"type": "string"},
        "company": {
            "type": "object",
            "properties": {
                "name": {"type": "string"}
            }
        }
    }
}

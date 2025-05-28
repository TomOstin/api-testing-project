from jsonschema import validate

def validate_user_schema(data: dict, schema: dict):
    """
    Обёртка над jsonschema.validate для валидации пользователя.
    Бросает ValidationError при несоответствии.
    """
    try:
        validate(instance=data, schema=schema)
    except Exception as e:
        raise AssertionError(f"Validation failed: {e}")
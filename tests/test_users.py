import pytest
import requests
from api.users_api import BASE_URL
from utils.validation import validate_user_schema
from api.users_api import get_all_users, get_user_by_id, get_users_by_city, create_user
from schemas.user_schema import user_schema

# Получаем всех пользователей один раз, чтобы использовать в параметризованных тестах
all_users = get_all_users()
user_ids = [user["id"] for user in all_users]


def test_api_available():
    """
    Проверяет, что API отвечает на базовый GET-запрос.
    Это первичная проверка, прежде чем запускать остальные тесты.
    """
    response = requests.get(f"{BASE_URL}/users", timeout=5)
    assert response.status_code == 200


def test_get_users():
    """
    Проверяет, что API возвращает список из 10 пользователей,
    каждый из которых соответствует схеме user_schema.
    """
    data = get_all_users()

    assert isinstance(data, list), "Expected list of users"
    assert len(data) == 10, f"Expected 10 users, got {len(data)}"

    for user in data:
        assert isinstance(user, dict), "Each user should be a dictionary"
        assert "id" in user, "User dict must contain 'id'"
        # Проверка соответствия каждого пользователя json-схеме
        validate_user_schema(user, user_schema)


@pytest.mark.parametrize("user_id", user_ids)
def test_get_single_user(user_id):
    """
    Проверяет, что API возвращает корректного пользователя по ID,
    и он соответствует схеме user_schema.
    """
    data = get_user_by_id(user_id)

    assert data["id"] == user_id
    assert "name" in data
    assert isinstance(data["name"], str)

    # Проверка структуры ответа на соответствие схеме
    validate_user_schema(data, user_schema)


@pytest.mark.parametrize("invalid_id", [-1, 0, 9999, "abc", None])
def test_get_user_invalid_id(invalid_id):
    """
    Проверяет, что API возвращает ошибку при запросе несуществующего или некорректного ID.
    """
    url = f"{BASE_URL}/users/{invalid_id}"
    response = requests.get(url)
    assert response.status_code in [400, 404], f"Unexpected status code: {response.status_code}"


def test_get_users_by_city_south_christy():
    """
    Проверяет, что в городе 'South Christy' живёт один пользователь — Mrs. Dennis Schulist
    """
    users = get_users_by_city("South Christy")

    assert len(users) == 1, f"Expected 1 user, got {len(users)}"
    user = users[0]
    assert user["name"] == "Mrs. Dennis Schulist"


def test_create_user():
    """
    Тестирует создание нового пользователя через POST-запрос.
    """
    user_dict = {
        'name': 'Jon',
        'username': 'Jonny',
        'email': 'jon@example.com',
    }

    response = create_user(user_dict)

    assert response.status_code in [201, 200], f"Unexpected status code: {response.status_code}"

    data = response.json()
    # Проверка, что значения совпадают с переданными
    assert data["name"] == "Jon"
    assert data["username"] == "Jonny"
    assert data["email"] == "jon@example.com"


def test_create_user_empty_payload():
    """
    Проверяет, что при создании пользователя с пустым телом запроса
    API не возвращает поля name, username, email в ответе.
    """
    invalid_create = {}

    response = create_user(invalid_create)

    # jsonplaceholder возвращает 201 даже на пустое тело — это ожидаемо
    assert response.status_code in [201, 200], f"Unexpected status code: {response.status_code}"

    data = response.json()

    # Проверяем, что отсутствующие поля остались пустыми
    assert data.get("name") is None
    assert data.get("username") is None
    assert data.get("email") is None


def test_create_user_invalid_types():
    """
    Демонстрирует, что jsonplaceholder принимает невалидные типы данных
    без ошибок. В реальном API это должно было вызвать 400 Bad Request.
    """
    invalid_user = {
        "name": 123,
        "email": True,
        "username": None
    }

    response = create_user(invalid_user)

    # В реальном API мы бы ожидали 400, но фейковый сервер возвращает 201
    assert response.status_code == 201

    data = response.json()

    # Проверка: API сохраняет мусор как есть
    assert data["name"] == 123
    assert data["email"] is True
    assert data["username"] is None


def test_create_user_missing_fields():
    """
    Проверяет, что при отсутствии обязательных полей name и email
    фейковый API не валится и возвращает 201 с неполными данными.
    В реальном API мы бы ожидали ошибку 400 Bad Request.
    """
    user_data = {
        "username": "ghost_user"
        # нет name и email
    }

    response = create_user(user_data)

    assert response.status_code == 201

    data = response.json()

    # Проверяем, что name и email отсутствуют, а username остался
    assert data.get("name") is None
    assert data.get("email") is None
    assert data["username"] == "ghost_user"


def test_users_have_unique_ids():
    """
    Проверяет, что у всех пользователей уникальные ID.
    Это стандартная проверка целостности данных.
    """
    users = get_all_users()
    ids = [user["id"] for user in users]

    # Получаем список дублирующихся ID (если есть)
    duplicates = [id for id in ids if ids.count(id) > 1]

    # Проверяем, что дубликатов нет
    assert len(ids) == len(set(ids)), f"Есть дубликаты ID: {duplicates}"

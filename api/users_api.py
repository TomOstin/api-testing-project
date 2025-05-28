import requests

# Базовый URL для тестового API
BASE_URL = "https://jsonplaceholder.typicode.com"


def get_all_users():
    """
    Выполняет GET-запрос к /users.
    Возвращает список всех пользователей в формате JSON.
    """
    response = requests.get(f"{BASE_URL}/users")
    response.raise_for_status()  # Бросает ошибку при статусе >= 400
    return response.json()


def get_user_by_id(user_id):
    """
    Выполняет GET-запрос к /users/{user_id}.
    Возвращает данные одного пользователя.
    """
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    response.raise_for_status()
    return response.json()


def get_users_by_city(city_name: str):
    """
    Возвращает список пользователей, у которых address.city совпадает с переданным названием города.
    """
    users = get_all_users()

    # Фильтрация пользователей по городу
    return [user for user in users if user.get("address", {}).get("city") == city_name]


def create_user(data: dict):
    """
    Выполняет POST-запрос для создания нового пользователя.
    Возвращает объект Response (чтобы вызвать .json() или проверить .status_code).
    """
    response = requests.post(f"{BASE_URL}/users", json=data)
    response.raise_for_status()
    return response

# 🧪 API Testing Project — JSONPlaceholder

![Python](https://img.shields.io/badge/python-3.10+-blue?logo=python)
![Pytest](https://img.shields.io/badge/tested_with-pytest-green?logo=pytest)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

Pet-проект по автоматизации тестирования REST API с помощью `Python + Pytest`.

Проект проверяет фейковый API [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com) и демонстрирует навыки:

- написания автотестов
- валидации данных
- обработки ошибок
- тест-дизайна и параметризации
- подготовки отчётов

---

## 🔍 Что покрыто тестами

- ✅ Получение всех пользователей `/users`
- ✅ Получение пользователя по ID `/users/{id}`
- ✅ Поиск пользователей по городу
- ✅ Проверка уникальности ID
- ✅ Создание пользователя (`POST /users`)
- ✅ Негативные кейсы (404, пустые поля, неправильные типы)
- ✅ Валидация структуры через `jsonschema`
- ✅ Smoke-тест: API отвечает
- ✅ HTML-отчёты с `pytest-html`

---

## 📁 Структура проекта

```
api_testing_project/
├── api/              # API-запросы
├── schemas/          # JSON-схемы
├── tests/            # Тесты Pytest
├── utils/            # Утилиты (валидация схем)
├── reports/          # HTML-отчёты
├── .venv/            # Виртуальное окружение (в .gitignore)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠 Установка и запуск

```bash
git clone https://github.com/TomOstin/api-testing-project.git
cd api-testing-project
python -m venv .venv
.venv\Scripts\activate           # для Windows
pip install -r requirements.txt
```

### ▶️ Запуск тестов

Запуск всех тестов:

```bash
pytest tests/
```

Создание HTML-отчёта:

```bash
pytest tests/ --html=reports/report.html
```

---

## 🧪 Пример теста

```python
def test_get_user_by_id():
    user = get_user_by_id(1)
    assert user["id"] == 1
    validate_user_schema(user, user_schema)
```

---

## 📊 Тестовый отчёт

Пример отчёта после запуска:

![Пример HTML отчёта](report_preview.png)

---

## ⚠️ Примечание

Проект работает с фейковым API, который не реализует реальную валидацию.  
Все POST-запросы "успешны", даже с некорректными данными — это поведение симуляции, а не ошибки проекта.

---

## 👨‍💻 Автор

**Tom Ostin**  
Python-разработчик и тестировщик  
[GitHub: TomOstin](https://github.com/TomOstin) / 
[Telegram: TomOstin](https://t.me/tom_ostin)

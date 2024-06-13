# Diploma Project: Task Tracker

Этот репозиторий содержит дипломный проект для трекера задач. Проект реализован с использованием FastAPI и SQLAlchemy, а также включает миграции базы данных с помощью Alembic.

## Структура проекта



```plaintext
diploma/
├── tasktracker/
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── views.py
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── alembic.ini
├── requirements.txt
├── .gitignore
├── .env
├── README.md
```



## Описание

- **tasktracker/**: Содержит код приложения для отслеживания задач.
  - **crud.py**: CRUD операции для сотрудников и задач.
  - **database.py**: Настройка базы данных и создание сессии.
  - **main.py**: Главный файл для запуска приложения FastAPI.
  - **models.py**: Определения моделей SQLAlchemy для сотрудников и задач.
  - **schemas.py**: Pydantic схемы для валидации данных.
  - **views.py**: Эндпоинты API.
  - **routers/**: Маршруты для сотрудников и задач.
    - **employees.py**: Маршруты для сотрудников.
    - **tasks.py**: Маршруты для задач.
- **alembic/**: Содержит скрипты миграции базы данных.
  - **env.py**: Конфигурация Alembic.
  - **script.py.mako**: Шаблон для создания скриптов миграции.
  - **versions/**: Директория для хранения версий миграций.
- **alembic.ini**: Конфигурационный файл для Alembic.
- **requirements.txt**: Список зависимостей проекта.
- **.gitignore**: Файл для исключения из отслеживания ненужных файлов и директорий.
- **.env**: Файл для хранения конфигурации базы данных.

## Установка

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/irinasiur/diploma.git
    cd diploma
    ```

2. Создайте и активируйте виртуальное окружение:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:

    ```sh
    pip install -r requirements.txt
    ```

4. Создайте файл `.env` в корне проекта и добавьте в него строку подключения к базе данных:

    ```sh
    echo "DATABASE_URL=postgresql://postgres:your_password@localhost/diploma" > .env
    ```

5. Примените миграции базы данных:

    ```sh
    alembic upgrade head
    ```

## Запуск приложения

Запустите приложение с помощью Uvicorn:

```sh
uvicorn tasktracker.main:app --reload
```

Перейдите по адресу http://127.0.0.1:8000/docs для доступа к документации Swagger UI и тестирования API.

Тестирование CRUD операций
Используйте Postman или Swagger UI для тестирования следующих операций:

Сотрудники
- Создание сотрудника: POST /employees/
- Получение всех сотрудников: GET /employees/
- Получение сотрудника по ID: GET /employees/{employee_id}
- Обновление сотрудника: PUT /employees/{employee_id}
- Удаление сотрудника: DELETE /employees/{employee_id}

Задачи
- Создание задачи: POST /tasks/
- Получение всех задач: GET /tasks/
- Получение задачи по ID: GET /tasks/{task_id}
- Обновление задачи: PUT /tasks/{task_id}
- Удаление задачи: DELETE /tasks/{task_id}


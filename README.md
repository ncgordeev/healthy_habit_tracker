<h3 align="center">Трекер полезных привычек</h3>

## О проекте

SPA веб-приложения трекер полезных привычек. Проект создан для приобретения полезных привычек. Вы можете создавать
привычки, выставлять периодичность и время выполнения и вам будет приходить уведомление в телеграм.

## Технологии
- [![Python](https://img.shields.io/badge/Python-092E20?style=flat&logo=Python)](https://www.python.org/)
- [![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=Django)](https://www.djangoproject.com/)
- [![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-092E20?style=flat)](https://www.django-rest-framework.org/)
- [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-092E20?style=flat&logo=PostgreSQL)](https://www.postgresql.org/)
- [![Celery](https://img.shields.io/badge/Celery-092E20?style=flat&logo=Celery)](https://docs.celeryq.dev/en/stable/)
- [![Redis](https://img.shields.io/badge/Redis-092E20?style=flat&logo=Redis)](https://redis.io/)
- [![CORS](https://img.shields.io/badge/CORS-092E20?style=flat)](https://pypi.org/project/django-cors-headers/)

## Настройка проекта

Для работы с проектом произведите базовые настройки.

### 1. Клонирование проекта

Клонируйте репозиторий используя следующую команду.

  ```sh
  git clone git@github.com:ncgordeev/healthy_habit_tracker.git
  ```

### 2. Настройка виртуального окружения и установка зависимостей

- Инструкция для работы через виртуальное окружение - poetry:

```text
poetry init - Создает виртуальное окружение
poetry shell - Активирует виртуальное окружение
poetry install - Устанавливает зависимости
```

- Инструкция для работы через виртуальное окружение - pip:

Создает виртуальное окружение:

```text
python3 -m venv venv
```

Активирует виртуальное окружение:

```text
source venv/bin/activate          # для Linux и Mac
venv\Scripts\activate.bat         # для Windows
```

Устанавливает зависимости:

```text
pip install -r requirements.txt
```

### 3. Редактирование .env.sample:

- В корне проекта переименуйте файл .env.sample в .env и отредактируйте параметры:
    ```text
    # Postgresql
    POSTGRES_ENGINE="postgresql_psycopg2" - используем psycopg
    DB_NAME="db_name" - название вашей БД
    DB_USER="postgres" - имя пользователя БД
    DB_PASSWORD="secret" - пароль пользователя БД
    DB_HOST="host" - можно указать "localhost" или "127.0.0.1"
    DB_PORT=port - указываете порт для подключения по умолчанию 5432

    # Django
    SECRET_KEY=secret_key - секретный ключ django проекта

    # Redis
    REDIS_HOST= - данные redis

    # Telegram API
    TELEGRAM_BOT_API_KEY='secret key' - секретный ключ для подключения бота Telegram
    ```

### 4. Настройка БД:

- Примените миграции:
  ```text
  python manage.py migrate
  ```

- Для создания суперюзера используйте команду:
  ```text
  python manage.py csu
  ```

- Установите Redis:

    - Linux команда:
   ```text
   sudo apt install redis; 
  или 
  sudo yum install redis;
   ```

    - macOS команда:
   ```text
   brew install redis;
   ```

  - Windows инструкция: [перейти на Redis docs](https://redis.io/docs/install/install-redis/install-redis-on-windows/)

## Использование

### Для запуска локально проекта наберите в терминале команду:
  ```text
  python manage.py runserver
  ```
  перейдите по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

- Для запуска Celery:

worker:
    ```
    celery -A config worker -l INFO
    ```

beat:
    ```
    celery -A config beat -l INFO -S django
    ```
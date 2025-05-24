# LiText

LiText — это микросервисное приложение для сохранения и обмена текстовыми блоками через временные ссылки.

## 📦 Установка и запуск

### 1. Клонируйте основной репозиторий:
```bash
git clone https://github.com/medin-misha/LiText.git
cd LiText
```

### 2. Клонируйте зависимости:
```bash
git clone https://github.com/medin-misha/LiText_text_saver.git
git clone https://github.com/medin-misha/Heshator.git
```

---

## ⚙️ Настройка переменных окружения

### Heshator
Перейдите в `./LiText/Heshator` и создайте файл `.env`:
```
redis_url="redis://hasher_redis:6379"
```
> Укажите адрес к Redis-серверу.

---

### LiText_text_saver
Перейдите в `./LiText/LiText_text_saver` и создайте файл `.env`:
```
MONGO_HOST="text_saver_mongodb:27017"
MONGO_USER="login"
MONGO_PASS="password"
```
> Укажите данные для подключения к MongoDB.

---

### LiText_backend
Перейдите в `./LiText/LiText_backend/litext_backend` и создайте файл `.env`:
```
# PostgreSQL
POSTGRES_USER="postgres_user"
POSTGRES_PASSWORD="postgres_password"
POSTGRES_DB="postgres_db"
POSTGRES_PORT="5432"
POSTGRES_URL="192.168.2.6"

# Секретный ключ Django
SECRET_KEY="your_secret_key_here"

# RabbitMQ
RABBIT_MQ_HOST="192.168.2.6"
RABBIT_MQ_PORT="5672"
RABBIT_MQ_USER="guest"
RABBIT_MQ_PASSWORD="guest"

# URL сервисов
HESHATOR_URL="http://192.168.2.6:5001"
TEXT_SAVER_URL="http://192.168.2.6:5000"
```

> ⚠️ Все хосты и URL-адреса должны быть абсолютными — такими, чтобы к ним можно было подключиться как из Docker-контейнеров, так и с вашей локальной машины.

---

## 🚀 Запуск проекта

1. Запустите все сервисы через `docker-compose`:
```bash
docker compose up --build
```

2. Примените миграции и запустите сервер Django:
```bash
cd LiText/LiText_backend
uv run manage.py migrate
uv run manage.py runserver
```

---

## 🔐 Аутентификация и работа с API

### Создание пользователя:
```http
POST /api/v1/users/
Content-Type: application/json

{
  "username": "misha",
  "email": "",  // необязательное поле
  "password": "mypassword"
}
```

### Получение токена:
```http
POST /api/v1/tokens/
Content-Type: application/json

{
  "username": "misha",
  "password": "mypassword"
}
```

Ответ:
```json
{
  "token": "76cf70e5e622301a76df50954379534ae63faa50"
}
```

Добавьте токен в заголовок:
```
Authorization: token 76cf70e5e622301a76df50954379534ae63faa50
```

---

## 📝 Работа с текстами

### Создание текстового блока:
```http
POST /api/v1/texts/
Authorization: token ...
Content-Type: application/json

{
  "text": "mytext"
}
```

### Получение списка текстов:
```http
GET /api/v1/texts/
Authorization: token ...
```

Ответ:
```json
[
  {
    "timestamp": "2025-05-24T18:33:41.113909Z",
    "archive": false,
    "pk": 1,
    "body": "mytext"
  }
]
```

---

## 🔗 Создание временных ссылок

### Создание:
```http
POST /api/v1/texts/links/
Content-Type: application/json

{
  "life_time": 20,
  "link": "",
  "block": 1
}
```

Ответ:
```json
{
  "pk": 1,
  "timestamp": "2025-05-24T18:38:41.478900Z",
  "life_time": 20,
  "link": "ac91c3979c50fade22407ba4ecad3cd4",
  "block": 1
}
```

### Получение текста по ссылке:
```http
GET /api/v1/texts/links/ac91c3979c50fade22407ba4ecad3cd4
```

Ответ:
```json
{
  "pk": 1,
  "block_id": 1,
  "timestamp": "2025-05-24T18:38:41.478900Z",
  "life_time": 20,
  "link": "ac91c3979c50fade22407ba4ecad3cd4",
  "block": {
    "timestamp": "2025-05-24T18:33:41.113909Z",
    "archive": false,
    "pk": 1,
    "body": "mytext"
  }
}
```

---

## ✅ Готово!
Приложение запущено и готово к использованию.

Дополнительные CRUD-функции реализованы, изучите документацию к API или код — всё просто 😉
![image](https://github.com/user-attachments/assets/e9a0b288-0826-4651-a7bf-b0887dda4ce8)

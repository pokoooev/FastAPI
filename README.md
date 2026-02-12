# Bookstore API

REST API для управления книгами и категориями на FastAPI + SQLAlchemy + PostgreSQL.

---

## Запуск API

### Предварительные требования
- Python 3.8+
- PostgreSQL 12+
- Установленный WSL (для Windows)

---

### 1. Настройка

```bash

# Создайте виртуальное окружение
python -m venv venv

# Активация (Linux/Mac/WSL)
source venv/bin/activate

# Активация (Windows)
# venv\Scripts\activate

# Установите зависимости
pip install -r requirements.txt
2. Настройка базы данных
bash
# Войдите в PostgreSQL
sudo -u postgres psql

# Создайте пользователя и базу данных
CREATE USER octagon WITH PASSWORD '12345';
CREATE DATABASE octagon_db OWNER octagon;
GRANT ALL PRIVILEGES ON DATABASE octagon_db TO octagon;

# Выход
\q
3. Файл .env
Создайте файл .env в корне проекта:

env
# PostgreSQL
DB_HOST=localhost
DB_PORT=5432
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345

4. Запуск проекта
bash
# Запуск через uvicorn
uvicorn app.main:app --reload


5. Проверка работы
text
http://127.0.0.1:8000
Ожидаемый ответ:
json
{
  "message": "Welcome to Bookstore API"
}
Документация Swagger:

text
http://127.0.0.1:8000/docs
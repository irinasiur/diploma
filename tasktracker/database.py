import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Загрузить переменные окружения из файла .env
load_dotenv()

# Получить URL базы данных из переменных окружения
DATABASE_URL = os.getenv("DATABASE_URL")

# Проверка, что переменная окружения DATABASE_URL установлена
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables")

# Создание движка SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей SQLAlchemy
Base = declarative_base()

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    APP_NAME = os.getenv("APP_NAME", "Samira Birthday")

    FLASK_ENV = os.getenv(
        "FLASK_ENV",
        "development"
    )

    DEBUG = os.getenv(
        "FLASK_DEBUG",
        "True"
    ).lower() == "true"

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "samira-birthday-secret-key"
    )

    DATABASE_URL = os.getenv("DATABASE_URL")

    if DATABASE_URL and DATABASE_URL.startswith("postgresql://"):
        DATABASE_URL = DATABASE_URL.replace(
            "postgresql://",
            "postgresql+psycopg://",
            1
        )

    SQLALCHEMY_DATABASE_URI = DATABASE_URL

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Gestion des connexions PostgreSQL / Neon
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_recycle": 300,
        "pool_timeout": 30,
    }
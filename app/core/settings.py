import os

DB_DRIVER = os.getenv("DB_DRIVER")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_POOL_SIZE = os.getenv("DB_POOL_SIZE")
DB_MAX_OVERFLOW = os.getenv("DB_MAX_OVERFLOW")
DB_ECHO_SQL = os.getenv("DB_ECHO_SQL")

# Application
APP_ENV = os.getenv("APP_ENV")
APP_HOST = os.getenv("APP_HOST")
APP_PORT = os.getenv("APP_PORT")
APP_DEBUG = os.getenv("APP_DEBUG")
APP_SECRET_KEY = os.getenv("APP_SECRET_KEY")
APP_CORS_ORIGINS = os.getenv("APP_CORS_ORIGINS")

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL")
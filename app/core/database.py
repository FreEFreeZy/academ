from pydantic import BaseSettings, Field

class DatabaseProperties(BaseSettings):
    driver: str = Field(..., alias="DB_DRIVER")
    host: str = Field(..., alias="DB_HOST")
    port: int = Field(..., alias="DB_PORT")
    name: str = Field(..., alias="DB_NAME")
    user: str = Field(..., alias="DB_USER")
    password: str = Field(..., alias="DB_PASSWORD")
    pool_size: int = Field(10, alias="DB_POOL_SIZE")
    max_overflow: int = Field(20, alias="DB_MAX_OVERFLOW")
    echo_sql: bool = Field(False, alias="DB_ECHO_SQL")
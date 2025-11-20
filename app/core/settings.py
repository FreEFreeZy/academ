import json
from pydantic import BaseModel, Field, field_validator

class Settings(BaseModel):
    db_driver: str = Field(..., alias="DB_DRIVER")
    db_host: str = Field(..., alias="DB_HOST")
    db_port: int = Field(..., alias="DB_PORT")
    db_name: str = Field(..., alias="DB_NAME")
    db_user: str = Field(..., alias="DB_USER")
    db_password: str = Field(..., alias="DB_PASSWORD")
    db_pool_size: int = Field(10, alias="DB_POOL_SIZE")
    db_max_overflow: int = Field(20, alias="DB_MAX_OVERFLOW")
    db_echo_sql: bool = Field(False, alias="DB_ECHO_SQL")

    app_env: str = Field(..., alias="APP_ENV")
    app_host: str = Field(..., alias="APP_HOST")
    app_port: str = Field(..., alias="APP_PORT")
    app_debug: str = Field(..., alias="APP_DEBUG")
    app_secret_key: str = Field(..., alias="APP_SECRET_KEY")
    app_cors_origins: str = Field(..., alias="APP_CORS_ORIGINS")
    app_log_level: str = Field(..., alias="LOG_LEVEL")

    def get_database(self) -> str:
        return f"postgresql+{self.db_driver}://{self.db_user}:{self.db_password}:{self.db_host}/{self.db_name}"

    @field_validator("app_cors_origins", mode='before')
    def parse_cors_origins(self, v) -> None:
        if isinstance(v, str):
            json.loads(v)
        return v

settings = Settings()
import os

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SECRET_KEY: str = Field(default=...)
    USER_ACCESS_TOKEN_NAME: str = Field(default=...)
    DB_NAME: str = Field(default=...)
    DB_USER: str = Field(default=...)
    DB_PASSWORD: str = Field(default="")
    DB_HOST: str = Field(default=...)
    DB_PORT: int = Field(default=...)

    @computed_field
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), "..", ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings: Settings = Settings()

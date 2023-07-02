from pathlib import Path
from sys import modules

from pydantic import BaseSettings

BASE_DIR = Path(__file__).parent.resolve()


class Settings(BaseSettings):
    """Application settings."""

    ENV: str = "production"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    OPENAI_APIKEY: str
    _BASE_URL: str = f"https://{HOST}:{PORT}"
    # quantity of workers for uvicorn
    WORKERS_COUNT: int = 1
    # Enable uvicorn reloading
    RELOAD: bool = True
    # Database settings
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    _DB_BASE: str = "test1"
    DB_ECHO: bool = False

    SECRET_KEY: str = "c8bb3d5b40e6e7d741d79a9ca5116052675843c370e92338e58eadb0d8e23f2ca3234c3cef978034a3218db2671f51dcbac3ba8069bd952717903f8b60405528"  # Replace with a strong secret key in production
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    @property
    def DB_BASE(self):
        return self._DB_BASE

    @property
    def BASE_URL(self) -> str:
        return self._BASE_URL if self._BASE_URL.endswith("/") else f"{self._BASE_URL}/"

    @property
    def DB_URL(self) -> str:
        """
        Assemble Database URL from settings.

        :return: Database URL.
        """

        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_BASE}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        fields = {
            "_BASE_URL": {
                "env": "BASE_URL",
            },
            "_DB_BASE": {
                "env": "DB_BASE",
            },
        }


class TestSettings(Settings):
    @property
    def DB_BASE(self):
        return f"{super().DB_BASE}_test"


settings = TestSettings() if "pytest" in modules else Settings()

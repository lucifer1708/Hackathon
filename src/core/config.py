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
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    _DB_BASE: str = "hackathon"
    DB_ECHO: bool = False

    SECRET_KEY: str  # Replace with a strong secret key in production
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    @property
    def DB_BASE(self):
        return self._DB_BASE

    @property
    def BASE_URL(self) -> str:
        return self._BASE_URL if self._BASE_URL.endswith("/") else f"{self._BASE_URL}/"

    @property
    def test_DB_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.DB_BASE}"

    @property
    def DB_URL(self) -> str:
        """
        Assemble Database URL from settings.

        :return: Database URL.
        """

        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.DB_BASE}"

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

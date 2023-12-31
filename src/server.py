import uvicorn
from src.core.config import settings


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        "src.core.app:get_app",
        workers=settings.WORKERS_COUNT,
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
        factory=True,
    )


if __name__ == "__main__":
    main()

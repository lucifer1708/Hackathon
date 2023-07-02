from src.api.router import api_router
from fastapi import FastAPI
from fastapi.responses import UJSONResponse


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="Hackathon Project",
        description="Kuch Desc daal do.. Plzz",
        version="1.0",
        docs_url="/docs/",
        redoc_url="/api/redoc/",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    app.include_router(router=api_router, prefix="/api")

    return app

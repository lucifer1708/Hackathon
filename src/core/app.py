from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from src.api.router import api_router


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="Career Intellect",
        description="The objective of our project is to extract relevant information from resume and present it in structured format. This project involves various stages of data processing, analysis and integration to provide an efficient and effective solution for automating the recruitment process.",
        version="1.0",
        docs_url="/docs/",
        redoc_url="/api/redoc/",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    app.include_router(router=api_router, prefix="/api")

    return app

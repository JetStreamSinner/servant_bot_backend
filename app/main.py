from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from app.api.routes.api import router as api_router
from app.core.settings.app_settings import get_app_settings


def get_application() -> FastAPI:
    app_settings = get_app_settings()
    app = FastAPI(**app_settings["application_kwargs"])

    app.add_middleware(CORSMiddleware,
                       allow_origins=app_settings["allowed_hosts"],
                       allow_credentials=True,
                       allow_methods="*",
                       allow_headers="*")

    app.include_router(router=api_router)
    return app


application = get_application()

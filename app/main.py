from fastapi import FastAPI
from app.api.routes.api import router as api_router


def get_application() -> FastAPI:
    app = FastAPI()
    app.include_router(router=api_router)
    return app


application = get_application()

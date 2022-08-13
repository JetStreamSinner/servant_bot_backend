from fastapi import APIRouter
from app.api.routes.services import services_router

router = APIRouter()
router.include_router(router=services_router)

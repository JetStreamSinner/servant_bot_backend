from typing import List

from fastapi import APIRouter

from app.models.schemas.service import Service, ServiceDeclaration
from app.api.dependencies.services import services_repository

services_router = APIRouter()


@services_router.get(path="/services_list", response_model=List[ServiceDeclaration])
async def services_list_handler():
    return services_repository.get_services_list()


@services_router.get(path="/service_info/{service_id}", response_model=Service)
async def services_list_handler(service_id: int):
    return services_repository.get_service_info(service_id=service_id)


@services_router.post(path="/add_task/{service_id}")
async def services_list_handler(service_id: int):
    return "Post task at {0} service".format(service_id)

from typing import List

from fastapi import APIRouter, HTTPException, Request, Depends

from app.api.dependencies.services import get_services_repository
from app.api.dependencies.task import push_task_to_service
from app.database.repositories.services import ServicesRepository
from app.models.schemas.service import ServiceOuter, ServiceDeclaration

services_router = APIRouter()


@services_router.get(path="/services_list", response_model=List[ServiceDeclaration])
async def services_list_handler(services_repository: ServicesRepository = Depends(dependency=get_services_repository)):
    return services_repository.get_services_list()


@services_router.get(path="/service_info/{service_id}", response_model=ServiceOuter)
async def services_list_handler(service_id: int,
                                services_repository: ServicesRepository = Depends(dependency=get_services_repository)):
    try:
        return services_repository.get_service_info(service_id=service_id)
    except RuntimeError:
        raise HTTPException(status_code=400, detail="Unknown service id")


@services_router.post(path="/add_task/{service_id}")
async def services_list_handler(service_id: int, request: Request,
                                services_repository: ServicesRepository = Depends(dependency=get_services_repository)):
    try:
        service_info = services_repository.get_service_info(service_id=service_id)
    except RuntimeError:
        raise HTTPException(status_code=400, detail="Unknown service id")
    service_url = service_info.service_url
    return push_task_to_service(service_url=service_url, payload=await request.json())

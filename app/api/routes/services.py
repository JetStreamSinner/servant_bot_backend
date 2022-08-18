from typing import List

from fastapi import APIRouter

from app.models.schemas.service import ServiceInner, ServiceOuter, ServiceDeclaration
from app.models.schemas.task import Task

from app.api.dependencies.services import services_repository
from app.api.dependencies.task import TaskHandler

services_router = APIRouter()


@services_router.get(path="/services_list", response_model=List[ServiceDeclaration])
async def services_list_handler():
    return services_repository.get_services_list()


@services_router.get(path="/service_info/{service_id}", response_model=ServiceOuter)
async def services_list_handler(service_id: int):
    return services_repository.get_service_info(service_id=service_id)


@services_router.post(path="/add_task/{service_id}")
async def services_list_handler(task: Task):
    service_info = services_repository.get_service_info(service_id=task.service_id)
    # TODO Should parse like ServiceInner model
    service_url = service_info["service_url"]
    handler = TaskHandler()
    task_result = handler.push_task(service_url=service_url, payload=task.arguments)
    return task_result

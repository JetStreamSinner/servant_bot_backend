from typing import List

from fastapi import APIRouter

from app.models.schemas.service import Service, ServiceDeclaration

services_router = APIRouter()


@services_router.get(path="/services_list", response_model=List[ServiceDeclaration])
async def services_list_handler():
    return [ServiceDeclaration(id=0, service_title="Title"), ServiceDeclaration(id=1, service_title="Title"),
            ServiceDeclaration(id=2, service_title="Title")]


@services_router.get(path="/service_info/{service_id}", response_model=Service)
async def services_list_handler(service_id: int):
    return Service(id=service_id, service_title="Title", service_description="Description",
                   state_machine=["command1", "command2", "command3"])


@services_router.post(path="/add_task/{service_id}")
async def services_list_handler(service_id: int):
    return "Post task at {0} service".format(service_id)

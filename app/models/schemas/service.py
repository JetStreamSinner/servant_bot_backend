from pydantic import BaseModel, Field
from typing import List


class ServiceDeclaration(BaseModel):
    id: int = Field(title="Service id")
    service_title: str = Field(title="Service title")


class Service(ServiceDeclaration):
    service_description: str = Field(title="Human readable service description")
    state_machine: List[str] = Field(title="List of commands for making request to service")

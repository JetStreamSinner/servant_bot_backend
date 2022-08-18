from pydantic import BaseModel, Field
from typing import List, Dict, Any


class ServiceDeclaration(BaseModel):
    service_id: int = Field(title="Service id")
    service_name: str = Field(title="Service title")


class Service(ServiceDeclaration):
    service_description: str = Field(title="Human readable service description")
    arguments: List[Dict[str, Any]] = Field(title="List of commands for making request to service")

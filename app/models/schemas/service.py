from typing import List, Dict, Any

from pydantic import BaseModel, Field


class ServiceDeclaration(BaseModel):
    service_id: int = Field(title="Service id")
    service_name: str = Field(title="Service title")


class ServiceOuter(ServiceDeclaration):
    service_description: str = Field(title="Human readable service description")
    arguments: List[Dict[str, Any]] = Field(title="List of commands for making request to service")


class ServiceInner(ServiceOuter):
    service_url: str = Field(title="Service url")

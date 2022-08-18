from typing import List, Dict, Any

from pydantic import BaseModel, Field


class TaskPayload(BaseModel):
    arguments: Dict[str, Any] = Field(title="Payload")


class Task(TaskPayload):
    service_id: int = Field(title="Service handler")

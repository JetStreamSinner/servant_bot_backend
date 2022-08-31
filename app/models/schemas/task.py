from typing import List, Dict, Any

from pydantic import BaseModel, Field


class Task(BaseModel):
    arguments: Dict[str, Any] = Field(title="Payload")

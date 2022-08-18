from typing import Dict, Any
from app.models.schemas.task import TaskPayload
import requests


class TaskHandler:

    def push_task(self, service_url: str, payload: Any) -> Any:
        job_router = "/do_job"
        target_url = service_url + job_router
        job_result = requests.post(url=target_url, json=payload)
        return job_result.json()

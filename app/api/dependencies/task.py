from typing import Any

import requests


def push_task_to_service(service_url: str, payload: Any) -> Any:
    job_router = "/do_job"
    target_url = service_url + job_router
    job_result = requests.post(url=target_url, json=payload)
    return job_result.json()

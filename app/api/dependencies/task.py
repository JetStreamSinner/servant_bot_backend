from typing import Any

import requests
from fastapi import status, HTTPException


def push_task_to_service(service_url: str, payload: Any) -> Any:
    job_router = "/do_job"
    target_url = service_url + job_router
    job_result = requests.post(url=target_url, json=payload)

    match job_result.status_code:
        case status.HTTP_422_UNPROCESSABLE_ENTITY:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Incorrect arguments")
        case status.HTTP_200_OK:
            pass
        case _:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Error occur when trying post task to service")

    return job_result.json()

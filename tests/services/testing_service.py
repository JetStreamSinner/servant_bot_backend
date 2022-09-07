from fastapi import FastAPI
from pydantic import BaseModel


class ServiceResponse(BaseModel):
    data: str
    type: str


class ServiceInput(BaseModel):
    argument1: int
    argument2: int


fake_service = FastAPI()


@fake_service.get("/me")
def test_service_info_handler():
    return {
        "service_name": "Test service",
        "service_description": "Test service description",
        "arguments": [
            {
                "argument_name": "First component",
                "argument_description": "First value to add",
                "type": "text"
            },
            {
                "argument_name": "Second component",
                "argument_description": "Second value to add",
                "type": "text"
            }
        ]
    }


@fake_service.post("/do_job", response_model=ServiceResponse)
def root_handler(job_info: ServiceInput):
    first_component = job_info.argument1
    second_component = job_info.argument2
    result = first_component + second_component
    return ServiceResponse(data=result, type="text")

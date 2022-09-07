import threading

import uvicorn
from fastapi import status
from fastapi.testclient import TestClient

from app.main import get_application
from tests.services.testing_service import fake_service

fake_service_host_in_db = "127.0.0.1"
fake_service_port_in_db = 16000
fake_service_thread = threading.Thread(
    target=lambda: uvicorn.run(app=fake_service, host=fake_service_host_in_db, port=fake_service_port_in_db),
    daemon=True)
fake_service_thread.start()

application = get_application()
backend_client = TestClient(app=application)
fake_service_client = TestClient(app=fake_service)


class TestApi:
    def test_services_list(self):
        backend_response = backend_client.get("/services_list")
        status_code = backend_response.status_code
        assert status_code == status.HTTP_200_OK

        fake_service_response = fake_service_client.get("/me")
        status_code = fake_service_response.status_code
        assert status_code == status.HTTP_200_OK

        fake_service_body = fake_service_response.json()
        backend_body = backend_response.json()
        assert fake_service_body["service_name"] == backend_body[0]["service_name"]

    def test_service_info_correct_id(self):
        fake_service_id = 1
        fake_service_url = "/service_info/{0}".format(fake_service_id)
        backend_response = backend_client.get(fake_service_url)
        assert backend_response.status_code == status.HTTP_200_OK

        fake_service_response = fake_service_client.get("/me")
        assert fake_service_response.status_code == status.HTTP_200_OK

        fake_service_body = fake_service_response.json()
        backend_body = backend_response.json()

        assert fake_service_body["service_name"] == backend_body["service_name"]
        assert fake_service_body["service_description"] == backend_body["service_description"]
        assert fake_service_body["arguments"] == backend_body["arguments"]

    def test_service_info_wrong_id(self):
        incorrect_service_id = -123
        fake_service_url = "/service_info/{0}".format(incorrect_service_id)
        backend_response = backend_client.get(fake_service_url)
        backend_body = backend_response.json()
        assert backend_response.status_code == status.HTTP_400_BAD_REQUEST
        assert backend_body == {
            "detail": "Unknown service id"
        }

    def test_service_do_job_correct_args(self):
        fake_service_id = 1
        fake_service_url = "/add_task/{0}".format(fake_service_id)
        input_args = {
            "argument1": 12,
            "argument2": 14
        }
        backend_response = backend_client.post(fake_service_url, json=input_args)
        assert backend_response.status_code == status.HTTP_200_OK

        body = backend_response.json()
        expected_result = 26
        expected_data_type = "text"
        assert int(body["data"]) == expected_result
        assert body["type"] == expected_data_type

    def test_service_do_job_bad_service_id(self):
        incorrect_service_id = -123
        fake_service_url = "/add_task/{0}".format(incorrect_service_id)
        input_args = {
            "argument1": 12,
            "argument2": 14
        }
        backend_response = backend_client.post(fake_service_url, json=input_args)
        assert backend_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_service_do_job_bad_args(self):
        fake_service_id = 1
        fake_service_url = "/add_task/{0}".format(fake_service_id)
        input_args = {
            "argument1": "hello",
            "argument2": "world"
        }
        backend_response = backend_client.post(fake_service_url, json=input_args)
        print(backend_response.json())
        assert backend_response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

from typing import Dict, Any

import requests
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.database.repositories.dependencies.service_info_provider import ServiceInfoProvider
from app.database.tables.base import Base
from app.database.tables.services import Services


def check_service_availability(url: str) -> bool:
    try:
        _ = requests.get(url)
    except requests.exceptions.ConnectionError:
        return False
    return True


class DatabaseProvider(ServiceInfoProvider):
    engine = None

    def __init__(self, uri: str):
        super().__init__(uri)
        self.init_connection(uri=self.uri)

    def get_database_engine(self, connection_string: str):
        if not connection_string:
            raise RuntimeError("Empty connection string")

        try:
            eng = create_engine(connection_string)
        except SQLAlchemyError:
            raise RuntimeError("Cannot open database with path {0}".format(connection_string))
        return eng

    def init_connection(self, uri: str):
        if self.engine:
            return
        self.engine = self.get_database_engine(connection_string=uri)
        Base.metadata.create_all(self.engine)

    def request_service_info(self, service_id: int, service_url: str) -> Dict[str, Any]:
        info_router = "/me"
        info_url = service_url + info_router
        service_request = requests.get(url=info_url)
        service_info = service_request.json()
        service_info["service_id"] = service_id
        service_info["service_url"] = service_url
        return service_info

    def read(self) -> Any:
        session = Session(bind=self.engine)
        services_endpoints = session.query(Services.id, Services.uri).all()
        services_info = [self.request_service_info(service_id, service_uri) for (service_id, service_uri) in
                         services_endpoints if check_service_availability(url=service_uri)]
        return services_info

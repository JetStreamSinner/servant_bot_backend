from typing import List

from app.database.repositories.base import BaseRepository
from app.models.schemas.service import ServiceDeclaration, ServiceInner


class ServicesRepository(BaseRepository):

    def get_services_list(self) -> List[ServiceDeclaration]:
        return [ServiceDeclaration(service_id=service["service_id"],
                                   service_name=service["service_name"]) for service in self.source]

    def get_service_info(self, service_id: int) -> ServiceInner:
        # TODO Should return ServiceInner model not a raw dictionary
        return self.source[service_id]

    def add_task(self, service_id: int, args: []):
        pass

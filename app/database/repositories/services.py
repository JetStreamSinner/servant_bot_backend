from typing import List

from app.database.repositories.base import BaseRepository
from app.models.schemas.service import ServiceDeclaration, ServiceInner


class ServicesRepository(BaseRepository):

    def get_services_list(self) -> List[ServiceDeclaration]:
        return [ServiceDeclaration(service_id=service["service_id"],
                                   service_name=service["service_name"]) for service in self.source]

    def get_service_info(self, service_id: int) -> ServiceInner:
        service_data = next((service_data for service_data in self.source if service_data["service_id"] == service_id),
                            {})
        if not service_data:
            raise RuntimeError("Bad service index")
        service_info = ServiceInner(service_id=service_id, service_name=service_data["service_name"],
                                    service_description=service_data["service_description"],
                                    arguments=service_data["arguments"],
                                    service_url=service_data["service_url"])
        return service_info

    def add_task(self, service_id: int, args: []):
        pass

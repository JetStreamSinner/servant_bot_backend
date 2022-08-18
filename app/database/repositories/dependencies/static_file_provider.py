import json
from typing import Dict, Any

from app.database.repositories.dependencies.service_info_provider import ServiceInfoProvider


class StaticFileProvider(ServiceInfoProvider):

    def read(self) -> Any:
        with open(self.uri, "r") as file_storage:
            raw = file_storage.read()
            source = json.loads(raw)
            return source

import json
from app.database.repositories.dependencies.service_info_provider import ServiceInfoProvider


class StaticFileProvider(ServiceInfoProvider):

    def read(self, uri: str):
        with open(uri, "r") as file_storage:
            raw = file_storage.read()
            source = json.loads(raw)
            return source

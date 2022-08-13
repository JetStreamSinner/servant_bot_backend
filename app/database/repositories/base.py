import json


class BaseRepository:
    def __init__(self, datasource_uri: str):
        with open(datasource_uri, "r") as file_storage:
            raw = file_storage.read()
            self.source = json.loads(raw)
        if not self.source:
            raise RuntimeError("Cannot open datasource")

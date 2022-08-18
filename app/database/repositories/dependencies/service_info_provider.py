import json
from typing import Dict, Any


class ServiceInfoProvider:

    def __init__(self, uri: str):
        self.uri = uri

    def read(self) -> Any:
        raise RuntimeError("Need to implement")

    def get_as_json(self) -> Any:
        # Using caching may be?
        return self.read()

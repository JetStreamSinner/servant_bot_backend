from typing import List, Dict, Any
from app.core.settings.base import BaseAppSettings, DatasourceTypes


class AppSettings(BaseAppSettings):
    title: str = "Router Service"
    docs_url: str = "/docs"
    version: str = "0.0.0"
    service_source_uri: str = ""
    service_source_type: DatasourceTypes = DatasourceTypes.file
    allowed_hosts: List[str] = ["*"]

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "docs_url": self.docs_url,
            "version": self.version
        }

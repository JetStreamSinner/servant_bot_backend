from app.core.settings.app import AppSettings
from app.core.settings.app import DatasourceTypes


class TestAppSettings(AppSettings):
    service_source_uri = ""
    source_type = DatasourceTypes.database


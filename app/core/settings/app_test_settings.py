from app.core.settings.app import AppSettings
from app.core.settings.app import DatasourceTypes


class AppTestSettings(AppSettings):
    service_source_uri = "sqlite:///tests/resources/test_database.db"
    service_source_type = DatasourceTypes.database

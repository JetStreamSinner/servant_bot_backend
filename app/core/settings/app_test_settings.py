from app.core.settings.app import AppSettings
from app.core.settings.app import DatasourceTypes


class AppTestSettings(AppSettings):
    service_source_uri = "sqlite:///app/resources/test_database.db"
    source_type = DatasourceTypes.database

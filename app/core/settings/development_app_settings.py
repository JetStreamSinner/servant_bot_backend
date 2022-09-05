from app.core.settings.app import AppSettings
from app.core.settings.app import DatasourceTypes


class DevelopmentAppSettings(AppSettings):
    service_source_uri = "sqlite:///app/resources/develop_database.db"
    source_type = DatasourceTypes.database

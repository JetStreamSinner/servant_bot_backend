from app.core.settings.app import AppSettings
from app.core.settings.app import DatasourceTypes


class AppDevelopmentSettings(AppSettings):
    service_source_uri = "sqlite:///app/resources/develop_database.db"
    service_source_type = DatasourceTypes.database

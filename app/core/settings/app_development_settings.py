from app.core.settings.app import AppSettings
from app.core.settings.app import DatasourceTypes


class AppDevelopmentSettings(AppSettings):
    # TODO Same as in test settings configure
    service_source_uri = "sqlite:///app/resources/develop_database.db?check_same_thread=False"
    service_source_type = DatasourceTypes.database

from app.core.settings.app import AppSettings
from app.core.settings.app import DatasourceTypes


class AppTestSettings(AppSettings):
    # TODO Using check_same_thread is just a hack.
    # TODO Need to rework system with repositories and data providers
    # TODO because repository object and accordingly database object
    # TODO recreated when call any endpoint happened
    service_source_uri = "sqlite:///tests/resources/test_database.db?check_same_thread=False"
    service_source_type = DatasourceTypes.database

from app.core.settings.base import DatasourceTypes
from app.database.repositories.dependencies.database_provider import DatabaseProvider
from app.database.repositories.dependencies.static_file_provider import StaticFileProvider


class BaseRepository:
    def __init__(self, source_uri: str, source_type: DatasourceTypes):
        self.source_uri = source_uri
        self.source_type = source_type
        self.source = {}
        self.update_datasource()

    def update_datasource(self):
        if self.source_type == DatasourceTypes.file:
            provider = StaticFileProvider(uri=self.source_uri)
        elif self.source_type == DatasourceTypes.database:
            provider = DatabaseProvider(uri=self.source_uri)
        else:
            raise RuntimeError("Unknown type")
        self.source = provider.read()

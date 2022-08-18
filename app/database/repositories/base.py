from app.core.settings.base import DatasourceTypes
from app.database.repositories.dependencies.static_file_provider import StaticFileProvider


class BaseRepository:
    def __init__(self, source_uri: str, source_type: DatasourceTypes):
        self.source = {}
        if source_type == DatasourceTypes.file:
            provider = StaticFileProvider()
            self.source = provider.read(uri=source_uri)
        elif source_type == DatasourceTypes.database:
            raise RuntimeError("Not implemented")
        else:
            raise RuntimeError("Unknown type")

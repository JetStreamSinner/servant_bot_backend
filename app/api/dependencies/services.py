import pathlib

from app.database.repositories.services import ServicesRepository
from app.core.settings.app import DatasourceTypes

datasource = pathlib.Path("app/resources/services_info.json")

services_repository: ServicesRepository = ServicesRepository(source_uri=datasource.as_posix(), source_type=DatasourceTypes.file)

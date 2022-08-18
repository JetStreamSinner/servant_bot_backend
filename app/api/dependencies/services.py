import pathlib

from app.database.repositories.services import ServicesRepository
from app.core.settings.app import DatasourceTypes

source_uri = "sqlite:///app/resources/develop_database.db"
source_type = DatasourceTypes.database

services_repository: ServicesRepository = ServicesRepository(source_uri=source_uri, source_type=source_type)

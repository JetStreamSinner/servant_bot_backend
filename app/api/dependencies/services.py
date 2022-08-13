import pathlib

from app.database.repositories.services import ServicesRepository

datasource = pathlib.Path("app/resources/services_info.json")

services_repository: ServicesRepository = ServicesRepository(datasource_uri=datasource.as_posix())

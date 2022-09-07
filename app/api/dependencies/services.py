from app.core.config import get_app_settings
from app.database.repositories.services import ServicesRepository

app_settings = get_app_settings()
source_uri = app_settings.service_source_uri
source_type = app_settings.service_source_type

services_repository: ServicesRepository = ServicesRepository(source_uri=source_uri, source_type=source_type)

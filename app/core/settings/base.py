from enum import Enum

from pydantic import BaseSettings


class DatasourceTypes(Enum):
    file: str = "file"
    database: str = "db"


class AppEnvTypes(Enum):
    production: str = "prod"
    development: str = "development"
    test: str = "test"


class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = AppEnvTypes.development

    class Config:
        env_file = ".env"

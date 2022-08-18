from enum import Enum

from pydantic import BaseSettings


class DatasourceTypes(Enum):
    file: str = "file"
    database: str = "db"


class BaseAppSettings(BaseSettings):

    class Config:
        env_file = ".env"

from app.core.settings.app import AppSettings
from app.core.settings.development_app_settings import DevelopmentAppSettings
from app.core.settings.test_app_settings import TestAppSettings

from app.core.settings.base import AppEnvTypes

environments = {
    AppEnvTypes.development: DevelopmentAppSettings,
    AppEnvTypes.test: TestAppSettings,
    AppEnvTypes.production: ""
}


def get_app_settings(app_env: AppEnvTypes) -> AppSettings:
    config = environments[app_env]
    return config()

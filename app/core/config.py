from app.core.settings.app import AppSettings
from app.core.settings.app_development_settings import AppDevelopmentSettings
from app.core.settings.app_test_settings import AppTestSettings

from app.core.settings.base import AppEnvTypes, BaseAppSettings

environments = {
    AppEnvTypes.development: AppDevelopmentSettings,
    AppEnvTypes.test: AppTestSettings,
    AppEnvTypes.production: ""
}


def get_app_settings() -> AppSettings:
    config = environments[BaseAppSettings().app_env]
    return config()

from app.core.settings.app import AppSettings
from app.core.settings.app_development_settings import AppDevelopmentSettings
from app.core.settings.app_test_settings import AppTestSettings

from app.core.settings.base import AppEnvTypes

environments = {
    AppEnvTypes.development: AppDevelopmentSettings,
    AppEnvTypes.test: AppTestSettings,
    AppEnvTypes.production: ""
}


def get_app_settings(app_env: AppEnvTypes) -> AppSettings:
    config = environments[app_env]
    return config()

import logging

from app.core.configurations.app import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True

    title: str = "Dev Home Sensors Data"

    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file = "dev.env"

from app.core.configurations.app import AppSettings


class ProdAppSettings(AppSettings):

    title: str = "Prod Home Sensors Data"

    class Config(AppSettings.Config):
        env_file = "prod.env"

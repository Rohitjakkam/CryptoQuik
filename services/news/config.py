from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


# Used in run.py
class Config(BaseSettings):
    """
    Configuration for the news service.
    """

    model_config = SettingsConfigDict(env_file='settings.env')
    kafka_broker_address: str
    kafka_topic: str
    polling_interval_sec: Optional[int] = (
        10  # How frequently the news data source checks for new updates from the CryptoPanic API.
    )


config = Config()


# Used in run.py and news_downloader.py
class CryptopanicConfig(BaseSettings):
    """
    Configuration for the Cryptopanic API.
    """

    model_config = SettingsConfigDict(env_file='cryptopanic_credentials.env')
    api_key: str


cryptopanic_config = CryptopanicConfig()

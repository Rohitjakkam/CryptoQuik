from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional, Literal


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file="settings.env")
    kafka_broker_address: str
    kafka_input_topic: str
    kafka_output_topic: str
    kafka_consumer_group: str
    candle_seconds: int
    emit_incomplete_candles: Optional[bool] = False
    data_source: Literal["live", "historical", "test"]


config = Config()

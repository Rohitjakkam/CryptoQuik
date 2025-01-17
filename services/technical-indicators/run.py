from quixstreams import Application
from loguru import logger
from candle import update_candles
from technical_indicators import compute_indicators


def main(
    kafka_broker_address: str,
    kafka_input_topic: str,
    kafka_output_topic: str,
    kafka_consumer_group: str,
    max_candles_in_state: int,
    candle_seconds: int,
):
    logger.info("Hello from technical-indicators!")

    app = Application(
        broker_address=kafka_broker_address,
        consumer_group=kafka_consumer_group,
    )

    input_topic = app.topic(
        name=kafka_input_topic,
        value_deserializer="json",
    )

    output_topic = app.topic(
        name=kafka_output_topic,
        value_serializer="json",
    )

    sdf = app.dataframe(topic=input_topic)

    sdf = sdf[sdf["candle_seconds"] == candle_seconds]

    sdf = sdf.apply(update_candles, stateful=True)

    sdf = sdf.apply(compute_indicators, stateful=True)

    sdf = sdf.update(lambda value: logger.debug(f"Final message: {value}"))

    sdf = sdf.to_topic(output_topic)

    app.run()


if __name__ == "__main__":
    from config import config

    main(
        kafka_broker_address=config.kafka_broker_address,
        kafka_input_topic=config.kafka_input_topic,
        kafka_output_topic=config.kafka_output_topic,
        kafka_consumer_group=config.kafka_consumer_group,
        max_candles_in_state=config.max_candles_in_state,
        candle_seconds=config.candle_seconds,
    )

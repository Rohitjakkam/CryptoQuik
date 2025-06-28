from quixstreams import Application

app = Application(
    broker_address="localhost:31234",
    consumer_group="example",
)

# Define a topic with a JSON serializer
topic = app.topic(name="my_topic",value_serializer="json")

with app.get_producer() as producer:

    while True:

        # 1. Fake event data
        event = {"id": "1","text":"Hello ji Namaste!"}

        # 2. Serialize the event data
        message = topic.serialize(key=event["id"], value=event)

        # 3. Produce the message to the topic
        producer.produce(
            topic=topic.name,
            value=message.value,
            key=message.key
        )

        import time
        time.sleep(1)
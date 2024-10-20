from typing import List
from quixstreams import Application
from loguru import logger
from hopsworks_api import push_value_to_feature_group
import json


# hej


def topic_to_feature_store(
        kafka_broker_address: str,
        kafka_input_topic: str,
        kafka_consumer_group: str,
        feature_group_name: str,
        feature_group_version: int,
        feature_group_primary_keys: List[str],
        feature_group_event_time: str,
        start_offline_materialization: bool,
        batch_size: int,
        read_from_beginning: bool = False  # New parameter
):
    logger.debug(f'Kafka broker address: {kafka_broker_address}')
    logger.debug(f'Kafka input topic: {kafka_input_topic}')
    logger.debug(f'Kafka consumer group: {kafka_consumer_group}')
    logger.debug(f'Reading from beginning: {read_from_beginning}')

    if read_from_beginning:
        app = Application(
            broker_address = kafka_broker_address,
            consumer_group = kafka_consumer_group,
            auto_offset_reset = 'earliest',  # Add this line
        )
    else:
        app = Application(
            broker_address = kafka_broker_address,
            consumer_group = kafka_consumer_group,
        )

    input_topic = app.topic(kafka_input_topic)

    batch = []

    with app.get_consumer() as consumer:
        consumer.subscribe(topics = [input_topic.name])
        logger.debug(f'Subscribed to topic {kafka_input_topic}')

        # If reading from beginning, perform a dummy poll and seek to beginning

        while True:
            msg = consumer.poll(0.1)
            # logger.debug(f'Polled message: {msg}')

            if msg is None:
                continue
            elif msg.error():
                logger.error('Kafka error:', msg.error())
                continue

            value = msg.value()
            value = json.loads(value.decode('utf-8'))
            batch.append(value)

            if len(batch) < batch_size:
                logger.debug(f'Batch has size {len(batch)} < {batch_size}')
                continue

            logger.debug(f'Batch has size {len(batch)} >= {batch_size} Pushing data to Feature Store')
            try:
                push_value_to_feature_group(
                    batch,
                    feature_group_name,
                    feature_group_version,
                    feature_group_primary_keys,
                    feature_group_event_time,
                    start_offline_materialization,
                )
                batch = []
                consumer.store_offsets(message = msg)
            except Exception as e:
                logger.error(f'Error pushing data to Feature Store: {e}')


if __name__ == "__main__":
    from config import config

    topic_to_feature_store(
        kafka_broker_address = config.kafka_broker_address,
        kafka_input_topic = config.kafka_input_topic,
        kafka_consumer_group = config.kafka_consumer_group,
        feature_group_name = config.feature_group_name,
        feature_group_version = config.feature_group_version,
        feature_group_primary_keys = config.feature_group_primary_keys,
        feature_group_event_time = config.feature_group_event_time,
        start_offline_materialization = config.start_offline_materialization,
        batch_size = config.batch_size,
        read_from_beginning = config.read_from_beginning,
    )

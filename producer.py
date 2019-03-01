import config as conf
from time import sleep
from wsgiref import headers

from kafka import KafkaProducer


def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')

    except Exception as ex:
        print('Exception in publishing message!')
        print(str(ex))


def connect_kafka_producer(host):
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=[host], api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting kafka')
        print(str(ex))
    finally:
        return _producer


def start_publishing_in_topic(topic, host, message):
    kafka_producer = connect_kafka_producer(host)
    i = 0
    try:
        while True:
            publish_message(kafka_producer, topic, f'message', str(i) + " : " + message)
            i += 1
            sleep(5)
    except Exception as ex:
        print(str(ex))
    finally:
        kafka_producer.close()


if __name__ == '__main__':
    start_publishing_in_topic(topic=conf.topic_name, host=conf.host, message=conf.message)

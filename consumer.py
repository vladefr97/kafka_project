from kafka import KafkaConsumer, TopicPartition
import config as conf


def start_listen_topic(topic, timeout=1000, host='localhost:9092', outfile=None):
    while True:
        con = KafkaConsumer(topic, auto_offset_reset='latest',
                            bootstrap_servers=host,
                            api_version=(0, 10), consumer_timeout_ms=timeout)
        for msg in con:
            print(msg.value)
            if outfile is not None:
                with open(outfile, 'w') as file:
                    file.write(f"I received message: {msg.value} ")


if __name__ == '__main__':
    start_listen_topic(topic=conf.topic_name, host=conf.host, timeout=1000, outfile='outfile')

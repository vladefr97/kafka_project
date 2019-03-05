# Название топика для kafka
topic_name = "test_topic"
# Порт для продюсера kafka
host = 'localhost:9092'
# Публикуемое сообщение
# message = "test message"
message = open('json_file.json', 'r').read()

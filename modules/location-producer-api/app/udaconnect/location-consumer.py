from kafka import KafkaConsumer


TOPIC_NAME = 'location'

consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    print (message)

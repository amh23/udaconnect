import os
import sys
from kafka import KafkaProducer


KAFKA_URL= os.environ["KAFKA_URL"]
TOPIC_NAME = os.environ["KAFKA_TOPIC"]
 

producer = KafkaProducer(bootstrap_servers=KAFKA_URL)

producer.send(TOPIC_NAME, b'Test Message!!!')
producer.flush()

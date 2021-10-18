import os
import json
from kafka import KafkaConsumer
from sqlalchemy import create_engine 

DB_USER = os.environ["DB_USERNAME"]
DB_PASSWORD  = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

KAFKA_URL = os.environ["KAFKA_URL"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC"]

consumer = KafkaConsumer(KAFKA_TOPIC,bootstrap_servers=[KAFKA_URL])

def save(location):
    engine = create_engine(
         f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
        echo=True
    )
    
    conn = engine.connect()

    person_id = int(location["person_id"])
    latitude, longitude = int(location["latitude"]), int(location["longitude"])

    save = "INSERT INTO location (person_id, coordinate) VALUES ({},ST_Point({}, {}))".format(person_id, latitude, longitude)
    print(save)
    conn.execute(save)

    for location in consumer:
        msg = location.value.decode('utf-8')
        print('{}'.format(msg))
        location_msg = json.loads(msg)
        save(location_msg)
import json
import pandas as pd
from kafka import KafkaConsumer

class Consumer:
    def __init__(self, topic):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    def consume(self):
        try:
            for message in self.consumer:
                flights = message.value
                yield flights
            self.consumer.close()
        except Exception as e:
            print(e)
            self.consumer.close()

def got_data():
    consumeFligths = Consumer('vuelos')
    dataFrame = None
    for message in consumeFligths.consume():
        dataFrame = pd.DataFrame(message)
        consumeFligths.consumer.close()
        break
    return dataFrame


#kafka-topics --create --topic vuelos --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092


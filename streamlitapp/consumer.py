import json
import pandas as pd
import time
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
                df = pd.DataFrame(flights)  
                yield df
            self.consumer.close()
        except Exception as e:
            print(e)
            self.consumer.close()

aviones = Consumer('mi-topic')            
for dataframe in aviones.consume():
    time.sleep(5)
    print(dataframe)

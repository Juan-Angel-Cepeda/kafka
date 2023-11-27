import json
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
        for message in self.consumer:
            yield message.value
            
flights_consumer = Consumer('mi-topic')
for message in flights_consumer.consume():
    print(message)

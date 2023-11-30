import json
import pandas as pd
from kafka import KafkaConsumer, TopicPartition

class Consumer:
    def __init__(self, topic, partition):
        partition_info = TopicPartition(topic, partition)
        self.consumer = KafkaConsumer(
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8')))
        
        self.consumer.assign([partition_info])

    def consume(self):
        try:
            for message in self.consumer:
                flights = message.value
                yield flights
            self.consumer.close()
        except Exception as e:
            print(e)
            self.consumer.close()

def got_data(part):
    consumeFligths = Consumer('vuelos',partition=part)
    dataFrame = None
    for message in consumeFligths.consume():
        dataFrame = pd.DataFrame(message)
        consumeFligths.consumer.close()
        break
    return dataFrame

#kafka-topics.sh --create --topic vuelos --partitions 3 --replication-factor 1 --bootstrap-server localhost:9092


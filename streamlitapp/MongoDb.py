from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import consumer as cs

uri = "mongodb://localhost:27017"
consumer = cs.Consumer('vuelos')

try:
    connection = MongoClient(uri, server_api=ServerApi(version='1'))
    vuelos_db = connection.vuelos_db
    vuelos_col = vuelos_db.vuelos

    for message in consumer.consume():
        message = json.loads(message)
        print(message)
        #for document in message:
        #    document = str(document)
        #    vuelos_col.insert_one(document)
            
    connection.close()
    
except Exception as e:
    print(e)



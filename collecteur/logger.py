import datetime
import os
from pymongo import MongoClient
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

load_dotenv()

from elastic.elastic_config import get_elastic_client
from mongo.mongo_config import get_mongo_collection


mongo_collection = get_mongo_collection()
es = get_elastic_client()

def collect_log(message):
    log = {
        "timestamp": datetime.datetime.utcnow(),
        "message": message,
        "niveau": "INFO"
    }

    # Insertion MongoDB
    mongo_collection.insert_one(log)

    # Insertion Elasticsearch
    es.index(index=os.getenv("ELASTIC_INDEX"), body=log)

if __name__ == "__main__":
    collect_log("Démarrage de l'application SIEM simplifié.")

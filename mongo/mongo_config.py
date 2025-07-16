import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_mongo_collection():
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client[os.getenv("MONGO_DB")]
    return db[os.getenv("MONGO_COLLECTION")]


if __name__ == "__main__":
    collect_log("Tentative d’injection test de log depuis le collecteur.")

import os
from elasticsearch import Elasticsearch

def get_elastic_client():
    host = os.getenv("ELASTIC_HOST", "localhost")
    port = os.getenv("ELASTIC_PORT", "9200")
    url = f"http://{host}:{port}"
    return Elasticsearch(hosts=[url])

from elasticsearch import Elasticsearch

ELASTIC_URL = "http://localhost:9200"
USERNAME = "elastic"
PASSWORD = "iAQX8Zd8"   # paste your password here

try:
    es = Elasticsearch(
        ELASTIC_URL,
        basic_auth=(USERNAME, PASSWORD)
    )

    if es.ping():
        print("✅ Connected to Elasticsearch successfully!")
        print("Cluster info:")
        print(es.info())
    else:
        print("❌ Connection failed")

except Exception as e:
    print("❌ Error:", e)
from fastapi import FastAPI
from elasticsearch import Elasticsearch
import uuid
from datetime import datetime

app = FastAPI()

es = Elasticsearch(
    "YOUR_ELASTIC_URL",
    api_key="YOUR_API_KEY"
)

@app.post("/create_task")
def create_task(project_id: str, description: str, assigned_to: str, deadline: str, priority: str):

    task_id = str(uuid.uuid4())

    doc = {
        "task_id": task_id,
        "project_id": project_id,
        "description": description,
        "assigned_to": assigned_to,
        "status": "pending",
        "deadline": deadline,
        "priority": priority,
        "created_at": datetime.utcnow()
    }

    es.index(index="tasks", id=task_id, document=doc)

    return {"status": "created", "task_id": task_id}

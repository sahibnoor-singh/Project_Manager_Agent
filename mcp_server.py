from mcp.server.fastmcp import FastMCP
from elasticsearch import Elasticsearch
import uuid
from datetime import datetime

# Create MCP server
mcp = FastMCP("project_manager")

# Connect Elasticsearch
es = Elasticsearch(
    "https://my-elasticsearch-project-f3843a.es.us-central1.gcp.elastic.cloud",
    api_key="UkVfQW1wd0JmMlREaXliWWI1SkQ6MHRVd2VsRFVNck82TVQwTm1GYS1EQQ=="
)

@mcp.tool()
def create_project(name: str, deadline: str, priority: str):
    """Create a new project"""

    project_id = str(uuid.uuid4())

    doc = {
        "project_id": project_id,
        "name": name,
        "deadline": deadline,
        "priority": priority,
        "progress": 0,
        "status": "active",
        "created_at": datetime.utcnow()
    }

    es.index(index="projects", id=project_id, document=doc)

    return {
        "status": "created",
        "project_id": project_id,
        "name": name
    }

# Run MCP server
app = mcp.sse_app
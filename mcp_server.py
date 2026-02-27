from fastmcp import FastMCP
from elasticsearch import Elasticsearch
from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.responses import JSONResponse
import uuid
from datetime import datetime

# Create MCP server
mcp = FastMCP("project_manager")

# Elasticsearch connection
es = Elasticsearch(
    "https://my-elasticsearch-project-f3843a.es.us-central1.gcp.elastic.cloud",
    api_key="MGZfcm5wd0I3RV94d2gweE9XbnA6UWJhR2VLZXFfLUJLdGRfVl9BMmFHQQ=="
)

# Tool: create project
@mcp.tool()
def create_project(name: str, description: str):
    try:
        project = {
            "id": str(uuid.uuid4()),
            "name": name,
            "description": description,
            "created_at": datetime.utcnow().isoformat()
        }

        es.index(
            index="projects",
            id=project["id"],
            document=project
        )

        return {
            "status": "success",
            "project": project
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

# Use streamable-http transport at root path for Elastic Agent Builder
app = mcp.http_app(path="/", transport="streamable-http")
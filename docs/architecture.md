# Architecture

## Overview

```
┌───────────────────┐         ┌───────────────────┐         ┌───────────────────┐
│                   │         │                   │         │                   │
│   Elastic Agent   │────────▶│    MCP Server     │────────▶│   Elasticsearch   │
│     Builder       │         │    (FastMCP)      │         │      Cloud        │
│                   │         │                   │         │                   │
└───────────────────┘         └───────────────────┘         └───────────────────┘
         │                             │                             │
         │                             │                             │
         ▼                             ▼                             ▼
   Claude Sonnet              Streamable HTTP              Projects, Tasks,
   4.5 Reasoning                Transport                  Team Members
```

## Components

### 1. Elastic Agent Builder
- Hosts the AI agent with Claude Sonnet 4.5
- Manages conversation context and memory
- Routes tool calls to MCP server

### 2. MCP Server (FastMCP)
- Exposes project management tools via MCP protocol
- Uses streamable-http transport for Elastic compatibility
- Handles authentication with Elasticsearch

### 3. Elasticsearch Cloud
- Stores projects, tasks, and team data
- Provides search and analytics via ES|QL
- Enables risk scoring calculations

## Data Flow

1. **User Input** → User sends natural language request to Agent
2. **Reasoning** → Claude Sonnet analyzes request and selects appropriate tool
3. **Tool Call** → Agent calls MCP server via streamable HTTP
4. **Execution** → MCP server performs Elasticsearch operation
5. **Response** → Results returned through the chain
6. **Output** → Agent formulates human-readable response

## Indices Schema

| Index | Purpose | Key Fields |
|-------|---------|------------|
| `projects` | Store project metadata | project_id, name, status, deadline, priority, progress |
| `tasks` | Store task details | task_id, project_id, description, assigned_to, status |
| `team_members` | Store team info | member_id, name, email, role, skills |


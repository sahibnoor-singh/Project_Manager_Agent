# Agent Design

## Purpose

Autonomous Project Manager agent that handles project creation, task management, and risk assessment without manual database operations.

## Capabilities

| Capability | Description |
|------------|-------------|
| **Create Projects** | Adds new projects with metadata to Elasticsearch |
| **Task Management** | Create/update tasks with assignments and deadlines |
| **Risk Analysis** | Calculates risk scores based on progress and deadlines |
| **Search** | Query projects and tasks using natural language |

## MCP Tools

### create_project

Creates a new project in Elasticsearch.

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | string | Project name |
| `description` | string | Project description |

**Returns:** Project ID, timestamp, confirmation status

---

## Risk Scoring Logic

```
risk_score = (100 - progress) / max(days_remaining, 1)
```

| Risk Level | Condition |
|------------|-----------|
| HIGH | risk_score > 20 |
| MEDIUM | risk_score between 10-20 |
| LOW | risk_score < 10 |

## Agent Behavior

- **Validation**: Validates inputs before operations
- **Structured Responses**: Returns clear, formatted responses
- **Error Handling**: Handles errors gracefully with helpful messages
- **Context Aware**: Remembers conversation context for follow-up queries

## Example Interactions

**User:** "Create a new project called Website Redesign with description Complete overhaul of company website"

**Agent:** 
- Calls `create_project` tool
- Stores data in `projects` index
- Returns project ID and confirmation


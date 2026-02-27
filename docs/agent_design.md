# Agent Design

## Purpose
Autonomous Project Manager agent that handles project creation, task management, and risk assessment without manual database operations.

## Capabilities
- **Create Projects**: Adds new projects with metadata to Elasticsearch
- **Task Management**: Create/update tasks with assignments and deadlines
- **Risk Analysis**: Calculates risk scores based on progress and deadlines
- **Search**: Query projects and tasks using natural language

## Tool Design

### create_project
- **Input**: name, description
- **Output**: Project ID, timestamp, confirmation
- **Index**: `projects`

### create_task (planned)
- **Input**: project_id, description, assigned_to, deadline, priority
- **Output**: Task ID, confirmation
- **Index**: `tasks`

## Risk Scoring Logic

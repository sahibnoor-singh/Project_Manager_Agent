# Architecture

## Overview

┌─────────────────┐       ┌──────────────┐      ┌─────────────────┐
│ Elastic Agent   │────▶ │ MCP Server   │────▶ │ Elasticsearch   │
│ Builder         │       │ (FastMCP)    │      │ Cloud           │
└─────────────────┘       └──────────────┘      └─────────────────┘
│ │
▼ ▼
Claude Sonnet Streamable HTTP
(Reasoning) Transport


## Components

### 1. Elastic Agent Builder
- Hosts the AI agent with Claude Sonnet 4.5
- Manages conversation context
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
1. User sends request to Agent
2. Agent reasons about the task
3. Agent calls appropriate MCP tool
4. MCP server executes Elasticsearch operation
5. Results returned to Agent
6. Agent formulates human-readable response

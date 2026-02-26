# ES|QL Intelligence Queries

## Overdue Tasks

```esql
FROM tasks
| WHERE deadline < NOW() AND status != "completed"
```
```workload distribution
FROM tasks
| STATS task_count = COUNT(*) BY assigned_to
| SORT task_count DESC
```
```Project Progress Analysis
FROM projects
| EVAL days_remaining = DATE_DIFF("days", NOW(), deadline)
| KEEP name, progress, days_remaining
```

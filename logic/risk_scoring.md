# Risk Scoring Model

Risk formula:

risk_score = (100 - progress) / max(days_remaining, 1)

##Risk categories:

- HIGH: risk_score > 20
- MEDIUM: risk_score 10-20
- LOW: risk_score < 10

## Agent Behavior
- Validates inputs before operations
- Returns structured responses
- Handles errors gracefully with helpful messages

## Factors considered:

• Progress percentage  
• Days remaining  
• Deadline proximity  

## Purpose:

Identify projects at risk of missing deadlines.

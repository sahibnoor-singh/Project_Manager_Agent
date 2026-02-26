
This proves intelligence layer design.

---

# 📁 4️⃣ logic/risk_scoring.md

Document your risk model.

Example:

```markdown
# Risk Scoring Model

Risk formula:

risk_score = (100 - progress) / max(days_remaining, 1)

Risk categories:

HIGH: risk_score > 20
MEDIUM: risk_score between 10–20
LOW: risk_score < 10

Factors considered:

• Progress percentage  
• Days remaining  
• Deadline proximity  

Purpose:

Identify projects at risk of missing deadlines.

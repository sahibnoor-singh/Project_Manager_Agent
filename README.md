## Autonomous Project Manager (Elastic Agent)
This project demonstrates an AI-powered project intelligence system built entirely using Elasticsearch Serverless and Elastic Agent Builder.

### Inspiration
Most teams rely on dashboards, spreadsheets, or manual check-ins to understand project health. These approaches are reactive, time-consuming, and often miss early warning signals.
This project was inspired by the idea of building an agent that thinks like a project manager — one that continuously analyzes project data, detects risks early, and clearly explains what is wrong and what should be done next.

### Scope of the project
Portfolio-level project overview
Deadline risk detection
Overdue task identification
Progress vs deadline mismatch analysis
Team workload distribution
Risk scoring (Low / Medium / High)
Executive summary generation
Actionable recommendations

### What This Agent Does
• Portfolio-level project overview
• Detects overdue tasks
• Identifies high-risk projects
• Analyzes workload distribution
• Compares progress vs deadlines
• Generates executive summaries
• Provides recommendations

### Architecture
Brain - Elastic Agent Builder
Memory - Elasticsearch Serverless
Intelligence: ES|QL + Search tools

### Setup 
1. Run `setup/create_indices.http`
2. Run `setup/seed_data.http`
3. Open Elastic Agent Builder
4. Ask questions like:
   - “My team has this task on this deadline”
   - “Which tasks are overdue?”
   - “Which team member is overloaded?”
   - “Generate an executive summary”

### Final Capability Scope
• Portfolio overview  
• Deadline risk detection  
• Overdue task detection  
• Progress vs deadline mismatch  
• Workload distribution analysis  
• Executive summary generation  
• Recommendation engine

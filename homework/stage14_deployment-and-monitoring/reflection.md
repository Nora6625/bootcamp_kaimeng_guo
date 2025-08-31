# Reflection on Model Deployment and Monitoring

## Risks if Deployed
Deploying the current mock regression model could face several credible risks. First, **data drift** may occur if the distribution of `feature1` or `feature2` shifts over time, leading to inaccurate predictions. Second, **schema changes** in incoming data (e.g., missing or extra columns) could break the pipeline. Third, **model degradation** may happen due to concept drift or insufficient retraining. Fourth, **system failures** like high API latency or request errors can disrupt service. Finally, **business metric misalignment** may arise if model predictions no longer align with user expectations or KPIs.

## Monitoring Metrics Across Layers
- **Data:** Track `freshness_minutes` (alert if >60 min), `null_rate` (alert if >5%), and `schema_hash` (alert on mismatch).  
- **Model:** Monitor rolling MAE on a 2-week window (alert if >0.1) and calibration error (alert if >0.05).  
- **System:** Log p95 API latency (alert if >250 ms) and error rate (alert if >1%).  
- **Business:** Track approval rate or other key KPI (alert if drops >10% from baseline).

## Ownership & Handoffs
- **Data Layer:** Analyst weekly review; alerts sent to data team Slack channel; first step: inspect recent batch for missing or corrupted records.  
- **Model Layer:** ML engineer owns retraining; triggers include 5% PSI on key features or rolling MAE > threshold; retraining cadence: biweekly.  
- **System Layer:** Platform on-call responsible for API uptime; first step on alert: check logs and restart services if needed.  
- **Business Layer:** Product manager monitors KPI dashboards; approves rollback or mitigation plans; issues logged in project Jira board.  

This structure ensures proactive detection of failures, clear alerting channels, and defined responsibilities, making deployment safer and maintainable.

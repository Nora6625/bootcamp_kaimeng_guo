# China Real Estate Market Trend Analysis
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
- In recent years, China’s real estate market has faced multiple challenges: housing prices remain high in some cities, demand is weakening, and developers are under mounting debt pressure. These issues not only affect individual homebuyers but also have broader implications for financial stability and macroeconomic development.
- This project aims to analyze historical market data to identify trends in housing prices, transaction volumes, and potential risk areas. By turning this data into clear visual insights, we can provide actionable guidance for policymakers, investors, and industry stakeholders.

## Stakeholder & User
- Primary Stakeholder: Local housing authorities and national real estate regulatory bodies responsible for market supervision and policy decisions.
- End User: Real estate companies, investors, and financial analysts who need market trend insights to optimize decisions and manage risks.

## Useful Answer & Decision
- Predictive & descriptive
- Metric: Forecasted home price indices, transaction volumes, developer default risk
- Artifact: Scenario-based dashboards, summary reports with risk bands, and decision triggers for portfolio adjustments or regulatory intervention

## Assumptions & Constraints
- Assumption: Historical transaction and official statistics data are mostly reliable.
- Constraints: Using publicly available data, so internal sales data from developers is unavailable.Data collection methods may vary across cities, requiring cleaning and standardization.

## Known Unknowns / Risks
- Risk: Some cities or secondary markets may have incomplete data, potentially biasing the analysis.
- Uncertainty: Policy interventions, interest rate changes, or economic shocks may rapidly alter market trends, so metrics need continuous updating.

## Lifecycle Mapping
- Identify hotspot and coldspot cities → Problem Framing & Scoping (Stage 01) → Deliverable: Project plan and analysis proposal
- Analyze price and transaction volume trends → Data Processing & Analysis (Stage 02) → Deliverable: Cleaned real estate market dataset
- Provide visual trend insights → Visualization & Reporting (Stage 03) → Deliverable: Interactive dashboard and stakeholder memo

## Repo Plan
- /data/: Store public real estate transaction data, price indices, government statistics
- /notebooks/: Exploration of data and analysis ideas
- /src/: Reusable data processing and analysis functions
- /docs/: Stakeholder memos, analysis reports, and final presentation mater



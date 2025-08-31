# Applied Financial Engineering — Framework Guide Template

This Framework Guide is a structured reflection tool.  
Fill it in as you progress through the course or at the end of your project.  
It will help you connect each stage of the **Applied Financial Engineering Lifecycle** to your own project, and create a portfolio-ready artifact.

---

## How to Use
- Each row corresponds to one stage in the lifecycle.  
- Use the prompts to guide your answers.  
- Be concise but specific — 2–4 sentences per cell is often enough.  
- This is **not a test prep sheet**. It’s a way to *document, reflect, and demonstrate* your process.

---

## Framework Guide Table

| Lifecycle Stage | What You Did | Challenges | Solutions / Decisions | Future Improvements |
|-----------------|--------------|------------|-----------------------|---------------------|
| **1. Problem Framing & Scoping** | Defined a mock regression project predicting target from synthetic features. | Ambiguity in selecting meaningful metrics for mock data. | Focused on simple RMSE/MAE metrics to evaluate predictions. | In future, frame objectives with clearer business alignment. |
| **2. Tooling Setup** | Configured Python environment with pandas, numpy, sklearn, matplotlib, Flask. | Dependency version conflicts and notebook reproducibility. | Used `requirements.txt` and virtual environments. | Automate environment setup with scripts or containerization. |
| **3. Python Fundamentals** | Applied data manipulation, plotting, and function design. | Limited experience with modular code and CLI interfaces. | Refactored functions into `/src/`, practiced logging and CLI wrappers. | Strengthen advanced Python skills: decorators, type hints, testing. |
| **4. Data Acquisition / Ingestion** | Generated synthetic data and saved to JSON/CSV. | Ensuring consistent schema and reproducibility. | Created reusable ingestion functions and checkpoints. | Add automated validation of input schemas. |
| **5. Data Storage** | Stored raw and cleaned datasets in `/data/` with versioned filenames. | Managing file paths and overwrites in notebooks. | Standardized storage paths and implemented idempotent writes. | Explore database storage for larger datasets. |
| **6. Data Preprocessing** | Normalized features, handled missing values. | Handling edge cases in synthetic nulls. | Applied consistent preprocessing pipeline and utility functions. | Integrate more robust imputation methods. |
| **7. Outlier Analysis** | Inspected extreme values in synthetic dataset. | Hard to distinguish true signal vs noise. | Used simple capping and logging for traceability. | Apply statistical tests or anomaly detection algorithms. |
| **8. Exploratory Data Analysis (EDA)** | Plotted distributions, correlations, and simple metrics. | Some insights were noisy due to random data. | Focused on patterns that could affect model inputs. | Include automated dashboards for EDA summaries. |
| **9. Feature Engineering** | Added synthetic interactions and lagged features. | Justifying feature relevance in mock data. | Evaluated feature importance using simple regression weights. | Experiment with domain-informed features for real datasets. |
| **10. Modeling (Regression / Time Series / Classification)** | Trained linear regression models using sklearn. | Overfitting on small dataset and hyperparameter tuning. | Cross-validation and simple regularization applied. | Test additional models like Random Forest or Ridge regression. |
| **11. Evaluation & Risk Communication** | Evaluated MAE and RMSE; communicated risk of small sample variability. | Explaining model uncertainty for synthetic data. | Visualized predictions vs true values and included warnings. | Add rolling metrics and confidence intervals. |
| **12. Results Reporting, Delivery Design & Stakeholder Communication** | Generated simple text and plots; optional dashboard. | Simplifying technical outputs for stakeholder clarity. | Used inline plots and concise reporting in notebooks. | Build interactive dashboard for real stakeholders. |
| **13. Productization** | Pickled trained model and reusable functions in `/src/`. | Ensuring reproducibility and modularity. | Defined clear folder structure and idempotent writes. | Add automated CI/CD pipeline for production. |
| **14. Deployment & Monitoring** | Deployed Flask API for predictions and plotting. | Handling API latency, error handling, model drift. | Implemented logging, monitoring metrics, and alerts. | Integrate dashboards for real-time monitoring and retraining triggers. |
| **15. Orchestration & System Design** | Defined task DAG: ingest → clean → train → report. | Managing dependencies and checkpoints. | Created logging/checkpoint plan and refactored CLI tasks. | Scale orchestration with workflow tools or scripts. |
| **16. Lifecycle Review & Reflection** | Reviewed all stages; polished repo with clean structure and README. | Time management and balancing automation vs manual tasks. | Standardized folder structure and documented pipeline thoroughly. | Next project: strengthen automation, testing, and dashboarding. |



---

## Reflection Prompts

- **Most difficult stage:** Deployment & Monitoring due to integrating Flask, logging, and alerting.  
- **Most rewarding stage:** Modeling and EDA, where predictions and insights came together.  
- **Stage connections:** Decisions on preprocessing directly impacted model performance; orchestration influenced reproducibility.  
- **If repeated:** Automate more ingestion, preprocessing, and reporting; integrate dashboards earlier.  
- **Skills to strengthen:** Advanced Python, API design, automated workflow orchestration, and interactive dashboards.  

---
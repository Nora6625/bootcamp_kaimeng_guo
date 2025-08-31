# Financial Predictive Modeling Project

## Project Overview
This project builds a predictive model to estimate key financial metrics using historical and synthetic data.  
It supports analysts and managers by providing actionable insights, scenario analysis, and improved forecasting accuracy.

## Stakeholders
- **Investment Analyst:** Uses model outputs for portfolio strategy; cares about accuracy and interpretability.  
- **Risk Manager:** Monitors potential exposure; cares about reliability and transparency.  
- **Team Lead / PM:** Oversees project progress; cares about reproducibility and workflow clarity.

## Data Storage

Our project follows a structured storage convention to ensure clarity and reproducibility:

### File Formats
- **CSV**: Primary format for tabular data (easy to load with pandas).
- **JSON**: Used when pulling from APIs with nested data.
- **Parquet (optional)**: For efficient storage of large datasets.

### How Data is Accessed
- File paths are **not hardcoded**.  
- Instead, environment variables defined in `.env` are used for flexibility and security.  
- Example (`.env`):
  ```ini
  DATA_PATH=./data/raw/

## Data Preprocessing

We developed reusable cleaning functions (stored in `/src/cleaning.py`) to ensure consistent and modular data preparation.  
Key steps include:
- **Column Standardization**: Converting column names to lowercase with underscores for consistency.
- **Missing Data Handling**: Dropping columns with excessive missingness (>40%) and filling others with median values.
- **Reproducibility**: Functions are designed to be re-applied to new datasets with minimal changes.

The preprocessing workflow is demonstrated in `notebooks/data_preprocessing.ipynb`, where raw data from `/data/raw/` is cleaned and saved to `/data/processed/`.  
Final cleaned dataset: `data/processed/ibm_daily_clean.csv`.

## Repository Structure
project/
│
├── data/         # Raw and processed datasets
├── src/          # Functions, modules
├── notebooks/    # Analysis and modeling notebooks
├── docs/         # Documentation, framework guides
├── model/        # Pickled models and outputs
├─reports/      # Visualizations and reports
├─README.md     # Project overview and lifecycle mapping
├─requirements.txt # Python dependencies
└─.gitignore    # Ignore sensitive/system files

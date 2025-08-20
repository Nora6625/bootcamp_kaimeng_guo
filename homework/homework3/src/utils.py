import pandas as pd

def get_summary_stats(df: pd.DataFrame, file_path: str, cat_col: str = None):
    desc = df.describe()
    if cat_col is not None and cat_col in df.columns:
        grouped = df.groupby(cat_col).mean(numeric_only=True).reset_index()
        grouped.to_csv(file_path)
    return desc,grouped

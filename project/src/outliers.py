import pandas as pd
import numpy as np

def handle_outliers(df: pd.DataFrame, column: str, method: str = "remove", threshold: float = 1.5) -> pd.DataFrame:
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - threshold * iqr
    upper = q3 + threshold * iqr

    mask = (df[column] < lower) | (df[column] > upper)
    n_outliers = mask.sum()

    if method == "remove":
        return df.loc[~mask].reset_index(drop=True)

    elif method == "flag":
        df = df.copy()
        df[f"{column}_is_outlier"] = mask
        return df

    elif method == "keep":
        print(f"[INFO] Column: {column}, Outliers detected: {n_outliers}")
        return df

    else:
        raise ValueError("method must be one of {'remove', 'flag', 'keep'}")

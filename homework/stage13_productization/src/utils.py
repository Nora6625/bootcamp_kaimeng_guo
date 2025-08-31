"""
Utility functions for data analysis and metrics calculation.
"""

import pandas as pd

def calculate_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate descriptive statistics for the given DataFrame.

    Args:
        df (pd.DataFrame): Input dataset

    Returns:
        pd.DataFrame: Summary statistics of the dataset
    """
    return df.describe()

import pandas as pd

def drop_missing_threshold(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """
    Drop columns with more than threshold fraction of missing values.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        threshold (float): Fraction of allowed missing values (0–1)
    
    Returns:
        pd.DataFrame: Cleaned DataFrame
    """
    return df.loc[:, df.isnull().mean() < threshold]

def fill_missing(df: pd.DataFrame, column: str, method: str = "mean") -> pd.DataFrame:
    """
    Fill missing values in a given column with a chosen method.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        column (str): Column name
        method (str): "mean", "median", "mode", or "ffill"
    
    Returns:
        pd.DataFrame: Updated DataFrame
    """
    if method == "mean":
        df[column] = df[column].fillna(df[column].mean())
    elif method == "median":
        df[column] = df[column].fillna(df[column].median())
    elif method == "mode":
        df[column] = df[column].fillna(df[column].mode()[0])
    elif method == "ffill":
        df[column] = df[column].fillna(method="ffill")
    return df

def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert column names to lowercase and replace spaces with underscores.
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df

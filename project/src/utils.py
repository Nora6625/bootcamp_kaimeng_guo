
import pandas as pd
from typing import Optional

def parse_date_column(df: pd.DataFrame, column: str, date_format: Optional[str]=None) -> pd.DataFrame:
    """
    Converts a column to datetime.
    Args:
        df (pd.DataFrame): input dataframe
        column (str): column name to convert
        date_format (str, optional): strftime format, default None for automatic inference
    Returns:
        pd.DataFrame: dataframe with converted datetime column
    """
    df = df.copy()
    df[column] = pd.to_datetime(df[column], format=date_format, errors='coerce')
    return df

def convert_column_type(df: pd.DataFrame, column: str, dtype: str) -> pd.DataFrame:
    """
    Converts a column to a specific dtype.
    Args:
        df (pd.DataFrame): input dataframe
        column (str): column name
        dtype (str): target type (e.g., 'float', 'int', 'str')
    Returns:
        pd.DataFrame: dataframe with converted column
    """
    df = df.copy()
    df[column] = df[column].astype(dtype, errors='ignore')
    return df

def fill_missing_values(df: pd.DataFrame, strategy: str='mean', columns: Optional[list]=None, fill_value=None) -> pd.DataFrame:
    """
    Fill missing values in specified columns.
    Args:
        df (pd.DataFrame): input dataframe
        strategy (str): 'mean', 'median', 'mode', or 'constant'
        columns (list, optional): list of columns to fill, default all numeric
        fill_value: used if strategy='constant'
    Returns:
        pd.DataFrame: dataframe with missing values filled
    """
    df = df.copy()
    target_cols = columns if columns else df.select_dtypes(include=['number']).columns.tolist()
    
    for col in target_cols:
        if strategy == 'mean':
            df[col] = df[col].fillna(df[col].mean())
        elif strategy == 'median':
            df[col] = df[col].fillna(df[col].median())
        elif strategy == 'mode':
            df[col] = df[col].fillna(df[col].mode()[0])
        elif strategy == 'constant':
            if fill_value is None:
                raise ValueError("fill_value must be provided when strategy='constant'")
            df[col] = df[col].fillna(fill_value)
        else:
            raise ValueError("strategy must be one of ['mean', 'median', 'mode', 'constant']")
    return df

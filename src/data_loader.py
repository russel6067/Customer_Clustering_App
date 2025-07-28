import pandas as pd
import os

def load_customer_data(filepath='data/mall_customers.csv'):
    """
    Load customer data from a CSV file and check for required columns.

    Parameters:
    - filepath (str): Relative path to the CSV file.

    Returns:
    - df (DataFrame): Loaded customer data.
    """
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found at {filepath}")

        df = pd.read_csv(filepath)

        required_columns = {'Annual Income (k$)', 'Spending Score (1-100)'}
        if not required_columns.issubset(df.columns):
            raise ValueError(f"Missing required columns: {required_columns - set(df.columns)}")

        return df

    except Exception as e:
        raise RuntimeError(f"Error loading data: {e}")

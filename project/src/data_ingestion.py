import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
DATA_PATH = os.getenv("DATA_PATH", "../data/raw/")

def fetch_sample_data():
    """
    Fetch sample stock data from a public API (e.g., Alpha Vantage demo).
    Saves the raw data to CSV in data/raw/.
    """
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "IBM",
        "apikey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")
    df.index.name = "date"

    # Save raw data
    os.makedirs(DATA_PATH, exist_ok=True)
    filename = os.path.join(DATA_PATH, "ibm_daily_raw.csv")
    df.to_csv(filename)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    fetch_sample_data()

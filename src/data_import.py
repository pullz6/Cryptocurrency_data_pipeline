import requests 
from dotenv import load_dotenv
import os
import pandas as pd

# Load variables from .env into os.environ
load_dotenv()

# Retrieve the key
api_key = os.getenv("MY_API_KEY")

if not api_key:
    raise ValueError("API Key not found!")
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey='+api_key
r = requests.get(url)
data = r.json()
print(data.keys())
df_meta = pd.DataFrame(data['Meta Data'], index=[0])
df = pd.DataFrame(data['Time Series (Daily)'])
print(df.head())
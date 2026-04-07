import requests 
from dotenv import load_dotenv
import os
import pandas as pd

# Load variables from .env into os.environ
def importing_to_df(): 
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
    df = pd.DataFrame(data['Time Series (Daily)']).T.reset_index()
    df = df.rename({
        'index' : 'date',
        '1. open':'open',
        '2. high':'high',
        '3. low':'low',
        '4. close':'close',
        '5. volume':'volume',
    },axis=1)
    df['company'] = pd.DataFrame(data['Meta Data'],index=[0])['2. Symbol'][0]
    df = df.astype({
        'open':'float',
        'high':'float',
        'low':'float',
        'close':'float',
        'volume':'float'
    })
    df['date']= pd.to_datetime(df['date'])
    return df

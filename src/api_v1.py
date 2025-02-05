import requests 
import pandas as pd

# chave API

api_key = 'GA91UFJFP6IAB2L4'

# paramêtros

symbol = 'GALP.LS'

url = 'https://www.alphavantage.co/query'

params = {
    'function': 'TIME_SERIES_MONTHLY_ADJUSTED',
    'symbol': symbol,
    'apikey': api_key,
    'datatype': 'json'
}

#fazendo a solicitação à API

response = requests.get(url, params=params)
data = response.json()

# processar os dados
time_series = data["Monthly Adjusted Time Series"]
df = pd.DataFrame.from_dict(time_series, orient = "index")
df.index = pd.to_datetime(df.index)
df.index.name = "date"
df = df[["1. open", "2. high", "3. low", "4. close", "5. adjusted close", "6. volume", "7. dividend amount"]]
df.columns = ["open", "high", "low", "close", "adjusted_close", "volume", "dividend_amount"]
df = df.sort_index() # ordena por data


#salvar meu csv

output_path = r"C:\Users\isabe\Desktop\EDIT\EDIT\Data Ops\Galp_Project\data\monthly_adjusted_data.csv"

df.to_csv(output_path)

print(df.head())
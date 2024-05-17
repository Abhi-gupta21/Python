import requests
import datetime
import html

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
apikey = 'SD0QW2T5PW1RI4P2'
parameters = {
    'symbol': STOCK,
    'apikey': apikey,
    'function': 'TIME_SERIES_DAILY'
}

response = requests.get('https://www.alphavantage.co/query', params = parameters)
response.raise_for_status()
data = response.json()
print(data)
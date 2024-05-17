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

last_ref = data['Meta Data']['3. Last Refreshed']
print(last_ref)

prev_last_ref_day = str(int(last_ref.split('-')[2]) - 1)
if int(prev_last_ref_day) < 10:
    prev_last_ref_day = '0' + str(prev_last_ref_day)

prev_last_ref = last_ref.split('-')[0] + '-' + last_ref.split('-')[1] + '-' + prev_last_ref_day

print(prev_last_ref)

diff = float(data['Time Series (Daily)'][last_ref]['4. close']) - float(data['Time Series (Daily)'][prev_last_ref]['4. close'])

percentage = (diff/float(data['Time Series (Daily)'][prev_last_ref]['4. close'])) * 100

print(percentage)

if percentage > 5 or percentage < -5:
    print("get news!")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if percentage > 5 or percentage < -5:
    apkey = '8db622b9f33148dd95f11032f1c1d8ee'
    parameters2 = {
        'q': 'tesla',
        'apiKey': apkey,
        'language': 'en'
    }

    response2 = requests.get('https://newsapi.org/v2/everything', params = parameters2)

    response2.raise_for_status()

    data2 = html.unescape(response2.json())


    for i in range(3):
        print(html.unescape(data2['articles'][i]['description']))
        print(html.unescape(data2['articles'][i]['content']))

        print('\n\n\n\n\n')



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


import requests
from datetime import datetime
from datetime import timedelta
from twilio.rest import Client
import sys
import os

# Import api script
sys.path.append(r"C:\Users\KD Tablet\Desktop\code\python\api_key_creator")
import api_key_creator


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

def get_yday():
    today = datetime.now().date()
    # today = datetime(2024,1,16).date()
    week_day = today.weekday()
    if week_day == 0:
        yday = today - timedelta(days=3)
        day_before = today - timedelta(days=4)
    elif week_day == 6:
        yday = today - timedelta(days=2)
        day_before = today - timedelta(days=3)
    elif week_day == 1:
        yday = today - timedelta(days=1)
        day_before = today - timedelta(days=4)
    else:
        yday = today - timedelta(days=1)
        day_before = today - timedelta(days=2)
    return (yday.strftime("%Y-%m-%d"), day_before.strftime("%Y-%m-%d"))

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_params = {
    "function": "TIME_SERIES_DAILY"
    , "symbol": STOCK
    , "interval": "compact"
    , "apikey": os.environ['ALPHA_API_KEY']
    , "datatype": "json"
}

url = "https://www.alphavantage.co/query"

dates = get_yday()

response = requests.get(url=url, params=alpha_params)
print(response.status_code)
data = response.json()['Time Series (Daily)']

yday_data = data[dates[0]]
day_before_data = data[dates[1]]

price_change = round(float(yday_data['4. close'])/float(day_before_data['4. close']) - 1, 2)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_url = "https://newsapi.org/v2/everything"
news_params = {
    "q": COMPANY_NAME
    , "language": "en"
    , "apiKey": os.environ['NEWS_API_KEY']
    , "totalResults": 3
}
if abs(price_change) > .01:
    response = requests.get(url=news_url, params=news_params)
    print(response.status_code)
    news_data = response.json()['articles'][:3]
    send_message = True

output_string = "\n\n".join([f"""{STOCK}: {"🔺" if price_change > 0 else "🔻"} {round(abs(price_change)*100)}%\nHeadline: {n['title']}\nBrief: {n['description']}""" for n in news_data])

print(output_string)
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
if send_message:
    client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
    message = client.messages \
                .create(
                    body=output_string
                    , from_= os.environ['TWILIO_NUMBER']
                    , to= os.environ['MY_NUMBER']
                 )
    
    print(message.status)

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


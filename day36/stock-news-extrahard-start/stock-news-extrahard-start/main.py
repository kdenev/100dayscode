import requests
from datetime import datetime
from datetime import timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "IBEJ7KAYWYYX6GO4"

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

print(get_yday())

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# params = {
#     "function": "TIME_SERIES_DAILY"
#     , "symbol": STOCK
#     , "interval": "compact"
#     , "apikey": API_KEY
#     , "datatype": "json"
# }

# url = "https://www.alphavantage.co/query"

# response = requests.get(url=url, params=params)
# print(response.status_code)
# data = response.json()['Time Series (Daily)']
# print(data)



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

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


import requests
import os
from datetime import datetime, timedelta
from twilio.rest import Client
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.env')
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
FIELD = "Time Series (Daily)"
IDX_REFER = "4. close"
NEWS_API_KEY= os.getenv("NEWS_API_KEY")
TWILIO_ACCOUNT_SID =  os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_API_KEY =  os.getenv("TWILIO_API_KEY")
SENT_NUMBER =  os.getenv("SENT_NUMBER")
FROM_NUMBER =  os.getenv("FROM_NUMBER")

# format https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo
STOCK_URL = "https://www.alphavantage.co/query"
# https://newsapi.org/v2/everything?q=bitcoin&apiKey=ce46a7c024d84cdb8af9f7faea460638
NEWS_API_URL = "https://newsapi.org/v2/everything"
params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "interval":"1day",
    "outputsize":"compact",
    "apikey": STOCK_API_KEY,
}
news_params = {
    "q":COMPANY_NAME,
    "apiKey" : NEWS_API_KEY,
    "pageSize": 3
}

NOW = datetime.now()
NOW_STR = NOW.strftime('%Y-%m-%d')
YESTERDAY_DATE = (NOW - timedelta(1)).strftime('%Y-%m-%d')
YESTERDAY = (NOW - timedelta(1)).weekday()
PREV = 2
if YESTERDAY == 0:
    PREV = 4
DAY_BEFORE_YESTERDAY = (NOW - timedelta(PREV)).strftime('%Y-%m-%d')

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(STOCK_URL,params=params)
response.raise_for_status()
print(response.json()[FIELD][YESTERDAY_DATE])
print(response.json()[FIELD][DAY_BEFORE_YESTERDAY])
yesteday_data = response.json()[FIELD][YESTERDAY_DATE][IDX_REFER]
day_before_yesteday_data = response.json()[FIELD][DAY_BEFORE_YESTERDAY][IDX_REFER]
print(type(yesteday_data),type(day_before_yesteday_data))
diff= float(yesteday_data)-float(day_before_yesteday_data)
print("test1",float(yesteday_data),float(day_before_yesteday_data),diff)
movement_up=True
if diff < 0 :
    movement_up = False
diff_perr = (abs(diff)/float(day_before_yesteday_data))*100
print("test2",diff_perr)

is_alert = False
if diff_perr <= 5 and diff_perr != 0:
    is_alert = True
    print("Getting Top 3 News")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
messages = []
if is_alert:
    response = requests.get(NEWS_API_URL,params=news_params)
    response.raise_for_status()
    messages = response.json()["articles"]
else:
    exit()

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
t_cli = Client(TWILIO_ACCOUNT_SID,TWILIO_API_KEY)

UP_SYMBOL = "🔺"
DOWN_SYMBOL = "🔻"
symbol = ""
if movement_up:
    symbol = UP_SYMBOL
else:
    symbol = DOWN_SYMBOL

for msg in messages:
    
    MSG_CONTENT = f"""TSLA: {symbol}{diff_perr:10.1f}%
    Headline: {msg["title"]}. 
    Brief: {msg["description"]}
    """
    print("sending message:",MSG_CONTENT)

    msg = t_cli.messages.create(
        from_=FROM_NUMBER,
        to=SENT_NUMBER,
        body=MSG_CONTENT,
    )

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



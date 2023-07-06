import datetime

import password
import requests
import datetime
import math

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

url = "https://www.alphavantage.co/query"

params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA",
    "apikey": password.apiKey
}


def giveDate(date: datetime):
    date = str(date).split(" ")[0]
    return date


def givePercentage(yesterdayValue, twoDaysAgoValue):
    if yesterdayValue - twoDaysAgoValue > 0:
        return "{:.2f}".format(((yesterdayValue - twoDaysAgoValue) / twoDaysAgoValue) * 100)
    else:
        return "{:.2f}".format(((twoDaysAgoValue - yesterdayValue) / yesterdayValue) * -100)


response = requests.get(url, params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
yesterday = giveDate(datetime.datetime.today() - datetime.timedelta(days=1))
twoDaysAgo = giveDate(datetime.datetime.today() - datetime.timedelta(days=2))
yesterdayValue = float(data[str(yesterday)]["4. close"])
twoDaysAgoValue = float(data[str(twoDaysAgo)]["4. close"])

if -5 < float(givePercentage(yesterdayValue, twoDaysAgoValue)) < 5:
    print("No news to search")
else:
    print("Get News")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

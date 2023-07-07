import html
import password
import requests
import datetime
import newsSelector
import twilioMessenger

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

url = "https://www.alphavantage.co/query"

params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": password.stockApiKey
}


def giveDate(date: datetime):
    date = str(date).split(" ")[0]
    return date


def givePercentage(yesterdayValue, twoDaysAgoValue):
    return ((yesterdayValue - twoDaysAgoValue) / twoDaysAgoValue) * 100


response = requests.get(url, params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
yesterday = giveDate(datetime.datetime.today() - datetime.timedelta(days=1))
twoDaysAgo = giveDate(datetime.datetime.today() - datetime.timedelta(days=2))
yesterdayValue = float(data[str(yesterday)]["4. close"])
twoDaysAgoValue = float(data[str(twoDaysAgo)]["4. close"])

# if the percentage has increased or decreased, send a message with the news of the past day
if -5 < givePercentage(yesterdayValue, twoDaysAgoValue) < 5:
    print("No news to search")
else:
    newsSelectorApp = newsSelector.NewsSelector(COMPANY_NAME, yesterday)
    data = newsSelectorApp.callNewsApi()
    formatted_articles = [f"Headline: {article['title']}. \n Brief: {article['description']}" for article in data]

    print(formatted_articles)

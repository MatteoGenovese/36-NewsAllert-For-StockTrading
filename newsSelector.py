import password
import requests
import html


class NewsSelector:

    def __init__(self, company, date):
        self.url = "https://newsapi.org/v2/everything"
        self.params = {
            "qInTitle": company,
            "from": date,
            "sortBy": "popularity",
            "apiKey": password.newsApiKey,
            "language": "en"
        }

    def callNewsApi(self):
        response = requests.get(self.url, self.params)
        response.raise_for_status()
        data = response.json()["articles"][:3]

        return data

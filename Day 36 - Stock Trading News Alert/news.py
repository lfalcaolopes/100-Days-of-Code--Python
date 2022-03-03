import requests
from datetime import datetime, timedelta

# API_TOKEN = "https://newsapi.org/account"


class News:
    def __init__(self):
        self.company_name = "Tesla"
        self.yesterday = str(datetime.now() - timedelta(1)).split(" ")[0]
        self.parameters = None
        self.news_data = None

    def get_news(self):
        self.parameters = {
            "qInTitle": self.company_name,
            "from": self.yesterday,
            "language": "en",
            "sortBy": "popularity",
            "apiKey": API_TOKEN
        }

        response = requests.get(url='https://newsapi.org/v2/everything', params=self.parameters)
        self.news_data = response.json()["articles"][:3]
        print(self.news_data)
        return self.news_data

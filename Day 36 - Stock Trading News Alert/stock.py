import requests
from datetime import datetime, timedelta


# API_TOKEN = "https://www.alphavantage.co/support/#api-key"
PERCENTAGE = 5/100


class Stock:
    def __init__(self):
        self.code = "TSLA"
        self.yesterday = str(datetime.now() - timedelta(1)).split(" ")[0]
        self.day_before = str(datetime.now() - timedelta(2)).split(" ")[0]
        self.percentage_variation = None
        self.symbol = None

        self.parameters = {
            "function": "TIME_SERIES_DAILY",
            "symbol": self.code,
            "apikey": API_TOKEN
        }

        response = requests.get("https://www.alphavantage.co/query", params=self.parameters)
        self.stock_data = response.json()["Time Series (Daily)"]

    def enough_variation(self):
        yesterdays_price = float(self.stock_data[self.yesterday]["4. close"])
        day_before_price = float(self.stock_data[self.day_before]["4. close"])

        self.percentage_variation = round(((yesterdays_price - day_before_price) / day_before_price) * 100, 2)
        if self.percentage_variation > 0:
            self.symbol = "🔺"
        else:
            self.symbol = "🔻"

        if abs(self.percentage_variation) >= PERCENTAGE:
            print("yes")
            return True
        else:
            return False

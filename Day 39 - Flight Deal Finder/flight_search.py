import requests
from datetime import datetime, timedelta

url = "https://tequila-api.kiwi.com/v2/search"

header = {
    # "apikey": "https://tequila.kiwi.com/portal/docs/tequila_api/search_api"
}


class FlightSearch:
    def __init__(self):
        start_date = (datetime.now() + timedelta(1)).strftime("%d/%m/%Y")
        max_date = (datetime.now() + timedelta(weeks=2)).strftime("%d/%m/%Y")

        self.formatted = {}
        self.ticket_list = None

        self.parameters = {
            "fly_from": "SSA",
            "date_from": start_date,
            "date_to": max_date,
            "max_stopovers": 2,
            "curr": "BRL",
            "limit": 1
        }

    def trip_info(self):
        response = requests.get(url, params=self.parameters, headers=header)
        data = response.json()["data"]

        for flight in data:
            city_to = flight["cityCodeTo"]
            date = flight["local_departure"].split("T")[0].split("-")

            self.formatted[city_to] = {
                "price": flight["price"],
                "cityFrom": flight["cityFrom"],
                "airportFrom": flight["flyFrom"],
                "cityTo": flight["cityTo"],
                "airportTo": flight["flyTo"],
                "date": f"{date[2]}-{date[1]}-{date[0]}",
                "link": flight["deep_link"]
            }

        return self.formatted

    def tickets(self, entry, begin, end):
        self.parameters["date_from"] = begin
        self.parameters["date_to"] = end

        for airport in entry:
            self.parameters["fly_to"] = airport

            self.ticket_list = self.trip_info()

        return self.ticket_list

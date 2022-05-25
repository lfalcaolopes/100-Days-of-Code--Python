import requests


class DataManager:
    def __init__(self):
        self.get_url = "https://api.sheety.co/9d5acd285f7610595936ae718741743d/flightDeals/price"

        self.header = {
            # "Authorization": "Bearer https://dashboard.sheety.co/#"
        }

        response = requests.get(self.get_url, headers=self.header)

        self.data = response.json()["price"]

    def airports(self):
        airport_list = [item["iataCode"] for item in self.data]

        return airport_list

    def max_price(self):
        price = {item["iataCode"]: item["lowestPrice"] for item in self.data}

        return price

    def is_missing(self):
        self.cities = {item["city"]: item["id"] for item in self.data if item["iataCode"] == ""}

        if len(self.cities) > 0:
            status = True
        else:
            status = False

        output = {
            "codes": self.cities,
            "status": status
        }

        return output

    def add_iata(self, codes):
        counter = 0
        for key, value in self.cities.items():

            put_url = f"https://api.sheety.co/9d5acd285f7610595936ae718741743d/flightDeals/price/{value}"

            entry = {
                "price": {
                    "iataCode": codes[counter]
                }
            }

            counter += 1

            requests.put(put_url, json=entry, headers=self.header)

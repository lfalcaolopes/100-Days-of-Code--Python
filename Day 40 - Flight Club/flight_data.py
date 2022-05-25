import requests

url = "https://tequila-api.kiwi.com/locations/query"

header = {
    # "apikey": "https://tequila.kiwi.com/portal/docs/tequila_api/search_api"
}


class FlightData:
    def __init__(self):
        self.parameters = {
            "limit": 1,
            "location_types": "city"
        }

        self.codes = []

    def get_iata(self, locations):
        for key, value in locations.items():
            self.parameters["term"] = key

            response = requests.get(url, params=self.parameters, headers=header)
            self.codes.append(response.json()["locations"][0]["code"])

        return self.codes

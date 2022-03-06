import requests

nutri_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutri_header = {
    # "x-app-id": "https://developer.nutritionix.com/admin/access_details",
    # "x-app-key": "https://developer.nutritionix.com/admin/access_details",
    "Content-Type": "application/json"
}


class Nutrition:
    def __init__(self):
        self.nutri_parameters = {
             "gender": "male",
             "weight_kg": 72,
             "height_cm": 172,
             "age": 22
            }

        self.nutri_response = None

    def info(self, entry):
        self.nutri_parameters = {
            "query": entry
        }

        self.nutri_response = requests.post(url=nutri_url, json=self.nutri_parameters, headers=nutri_header)

        return self.nutri_response.json()["exercises"]

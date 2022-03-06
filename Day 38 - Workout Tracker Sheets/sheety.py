import requests
from datetime import datetime
import os

get_endpoint = "https://api.sheety.co/9d5acd285f7610595936ae718741743d/myPythonWorkouts/workouts"
post_endpoint = "https://api.sheety.co/9d5acd285f7610595936ae718741743d/myPythonWorkouts/workouts"

header = {
    # "Authorization": "Bearer https://dashboard.sheety.co/#"
}


class Sheety:
    def __init__(self):
        now = datetime.now()
        self.date = now.strftime("%d/%m/%Y")
        self.hour_now = now.strftime("%X")

    def update_sheet(self, **kwargs):
        workout = {
            'workout': {
                'date': self.date,
                'time': self.hour_now,
                'exercise': kwargs.get("exercise"),
                'duration': kwargs.get("duration"),
                'calories': kwargs.get("calories"),
                'id': 2
            }
        }

        requests.post(post_endpoint, json=workout, headers=header)

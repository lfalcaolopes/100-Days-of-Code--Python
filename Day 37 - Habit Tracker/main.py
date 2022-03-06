import requests
from datetime import datetime

url = "https://pixe.la/v1/users"


user_parameters = {
    "token": "qwertyuiop",
    "username": "kutinhas",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# created user
# response = requests.post(url=url, json=parameters)

endpoint = "https://pixe.la/v1/users/kutinhas/graphs"

headers = {
    "X-USER-TOKEN": "qwertyuiop",
}

graph_params = {
    "id": "happy",
    "name": "Happyness level",
    "unit": "points",
    "type": "int",
    "color": "shibafu"
}

# created graph
# response = requests.post(url=endpoint, json=graph_params, headers=headers)

pixel_endpoint = "https://pixe.la/v1/users/kutinhas/graphs/happy"

now = datetime.now()
date_today = now.strftime("%Y%m%d")

print(date_today)

pixel_params = {
    "date": date_today,
    "quantity": "7"
}

# create a pixel
# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)


edit_pixel_endpoint = f"https://pixe.la/v1/users/kutinhas/graphs/happy/{date_today}"

# edit a pixel
response = requests.put(url=pixel_endpoint, json=pixel_params, headers=headers)

print(response.text)
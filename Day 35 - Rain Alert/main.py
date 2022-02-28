import requests
from twilio.rest import Client

# my_key = "https://home.openweathermap.org/api_keys"
my_lat = -14.864970
my_long = -40.837200
# twilio_SID = "https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1"
# twilio_token = "https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1"
phone = +17853673661

parameters = {
    "lat": my_lat,
    "lon": my_long,
    "exclude": "current,minutely,daily,alerts",
    "appid": my_key,
    "units": "metric"
}

data = requests.get(f"https://api.openweathermap.org/data/2.5/onecall", params=parameters)
weather_data = data.json()

bigger_id = 0
is_raining = False

for index in range(12):
    weather_id = weather_data["hourly"][index]["weather"][0]["id"]
    weather_info = weather_data["hourly"][index]["weather"][0]["main"]
    weather_description = weather_data["hourly"][index]["weather"][0]["description"]

    if weather_id < 1000:
        text = f"Take your coat. There will be a {weather_description} today"

        is_raining = True


if is_raining:
    client = Client(twilio_SID, twilio_token)

    message = client.messages.create(
        body=text,
        from_='whatsapp:+14155238886',
        to='whatsapp:+557788532440'
    )

    print(message.status)

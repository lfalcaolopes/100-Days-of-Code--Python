# if the ISS is close to me
# and is past the sunset
# send me an email telling to look up
# run every 60 seconds

import requests
import smtplib
import datetime

MY_LAT = -14.864970
MY_LONG = -40.837200

my_email = "tp******12@gmail.com"
password = "ar***********s"

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}

sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
iss = requests.get(url="http://api.open-notify.org/iss-now.json")
sun_data = sun.json()
iss_data = iss.json()

iss_lat = iss_data["iss_position"]["latitude"]
iss_long = iss_data["iss_position"]["longitude"]

sunrise_hour = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hour = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

hour_now = datetime.datetime.now().hour
print(sunrise_hour)
print(sunset_hour)

if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LONG-5 <= iss_long <= MY_LONG+5 and (hour_now <= sunrise_hour or
                                                                               hour_now >= sunset_hour):
    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(user=my_email, password=password)
        connect.sendmail(from_addr=my_email,
                         to_addrs="l**********il.com",
                         msg=f"Subject:ISS in the skies NOW!\n\nLook up, you should be able to see the ISS satellite now"
                         )

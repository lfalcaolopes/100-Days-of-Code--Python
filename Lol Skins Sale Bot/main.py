import requests
from bs4 import BeautifulSoup
import smtplib

email = "skinsdolol23@gmail.com"
senha = "mnkwrkvdgyrkeoyf"

try:
    url = "https://tecmasters.com.br/?s=League+of+Legends%3A+as+promo%C3%A7%C3%B5es+da+semana+"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    lastSale = soup.find(name="div", class_="first").find('a').attrs['href']# BeautifulSoup

    response = requests.get(lastSale)
    soupSale = BeautifulSoup(response.text, "html.parser")
except:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connect: # smtplib
        connect.starttls()
        connect.login(user=email, password=senha)
        connect.sendmail(from_addr=email,
                         to_addrs="matheus7582@hotmail.com",
                         msg=f"Subject:F!\n\nSe fudeu pai".encode()
                         )

skinsList = [item.text for item in soupSale.find(name="div", class_="postContent").findAll('li')] # BeautifulSoup


champsIWant = ['Nilah', 'Zeri']

skinsIWantInSale = []

for skin in skinsList:
    for champ in champsIWant:
        if champ in skin:
            skinsIWantInSale.append(skin)

skinsIWantInSale = [(item.replace('–', '-')) for item in skinsIWantInSale]



if skinsIWantInSale:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connect: # smtplib
        connect.starttls()
        connect.login(user=email, password=senha)
        connect.sendmail(from_addr=email,
                         to_addrs="matheus7582@hotmail.com",
                         msg=f"Subject:Skin em promo!\n\n{skinsIWantInSale}\n Corre".encode()
                         )

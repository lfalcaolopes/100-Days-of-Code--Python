import requests
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com.br/Olympikus-43607875-T%C3%AAnis-Fibra/dp/B0961LX3LG/ref=sr_1_5?cs_asins=B08Z48QNCJ%2CB0961LX3LG%2CB0977PR7V3%2CB0961ZY2S9&cs_colors=242124%2C51585E%2C555555%2C1E2321&i_fs=0&i_im=1&i_ims=1&offset=4&qid=1645106492&ref_override=sr_1_5&refinements=p_85%3A19171728011&rnid=19171727011&rps=1&rrid=3EMB1SFX3CFBB6CM9ZNE&sr=1-5&srcWidgetTemplate=SEARCH_RESULTS&ufe=app_do%3Aamzn1.fos.db68964d-7c0e-4bb2-a95c-e5cb9e32eb12&th=1&psc=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7"
}

# my_email = "tpy*******2@gmail.com"
# password = "a***********s"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

current_price = int(soup.find("span", class_="a-price-whole").getText().replace(",", ""))

product_name = soup.title.getText().split(" | ")[0]

if current_price <= 280:
    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(user=my_email, password=password)
        connect.sendmail(from_addr=my_email,
                         # to_addrs="l********s@gmail.com",
                         msg=f"Subject:{product_name} is at discount!\n\n{product_name} is selling for "
                             f"R${current_price} right now!\n{url}".encode('utf-8')
                         )
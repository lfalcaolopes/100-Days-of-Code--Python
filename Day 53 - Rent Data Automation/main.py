from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
from time import sleep


listings_url = "https://www.zapimoveis.com.br/aluguel/apartamentos/ba+salvador++pituba/2-quartos/?banheiros=1&quartos=2&transacao=Aluguel&vagas=1&precoMaximo=3000&tipoUnidade=Residencial,Apartamento&tipo=Im%C3%B3vel%20usado&pagina=1&onde=,Bahia,Salvador,,Pituba,,,neighborhood,BR%3EBahia%3ENULL%3ESalvador%3EBarrios%3EPituba,-13.002606,-38.459277,"

forms_url = "https://docs.google.com/forms/d/e/1FAIpQLSfuIuWAPUIgRGSDX5AjCCZxlmfcS0q4YL6aLz8SwbhHcegEIQ/viewform?usp=sf_link"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7"
}


class RentData:
    def __init__(self):
        response = requests.get(listings_url, headers=headers)
        self.soup = BeautifulSoup(response.text, "html.parser")
        self.listings = None

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def get_listings(self):
        rent = self.soup.find_all(name="p", class_="simple-card__price")

        prices = [item.getText().split()[1].replace(".", "") for item in rent]


        listings_price = [item.get_text().split("\n")[1].split(" ")[-1] for item in prices]

        address = self.soup.find_all(name="h2", class_="simple-card__address")
        listings_location = [" ".join(item.get_text().split("\n")[1].split()) for item in address]

        ids = self.soup.find_all(name="div", class_="card-container")
        listings_website = [f'https://www.zapimoveis.com.br/imovel/{item.get("data-id")}' for item in ids]

        self.listings = {
            "price": listings_price,
            "location": listings_location,
            "url": listings_website
        }

    def post_listings(self):
        self.driver.get(forms_url)

        sleep(2)

        for counter in range(len(self.listings["price"])):
            text_inputs = self.driver.find_elements(By.CSS_SELECTOR, ".quantumWizTextinputPaperinputInput")

            text_inputs[0].send_keys(self.listings["location"][counter])
            sleep(0.25)
            text_inputs[1].send_keys(self.listings["price"][counter])
            sleep(0.25)
            text_inputs[2].send_keys(self.listings["url"][counter])
            sleep(0.25)

            send = self.driver.find_element(By.CSS_SELECTOR, ".appsMaterialWizButtonPaperbuttonLabel")
            send.click()

            sleep(1)

            submit_other_response = self.driver.find_element(By.CSS_SELECTOR, ".freebirdFormviewerViewResponseLinksContainer a")
            submit_other_response.click()

            sleep(2)
            print("click")


bot = RentData()
bot.get_listings()
bot.post_listings()

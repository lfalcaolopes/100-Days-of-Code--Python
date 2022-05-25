import requests
from bs4 import BeautifulSoup
import random

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all(name="h3", class_="title")

film_list = [item.getText() for item in titles]
formatted_list = film_list[::-1]

print(random.choice(formatted_list))


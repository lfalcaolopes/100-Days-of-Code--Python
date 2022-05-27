from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element(By.ID, "bigCookie")

base = 1
increment = 0.1
timeout = time.time() + base

while True:
    cookie.click()

    if time.time() > timeout:

        upgrades_list = driver.find_elements(By.CSS_SELECTOR, "#upgrades .enabled")
        upgrades = [item.text for item in upgrades_list]

        if len(upgrades) > 0:
            shop = driver.find_element(By.ID, f"upgrade{len(upgrades) - 1}")
            shop.click()

        products_list = driver.find_elements(By.CSS_SELECTOR, ".enabled .price")
        products = [item.text for item in products_list]

        if len(products) > 0:
            shop = driver.find_element(By.ID, f"product{len(products) - 1}")
            shop.click()

        if (len(products) - 1) == 0:
            timeout = time.time() + 1
        else:
            base += increment

            timeout = time.time() + base

        print(base)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://tinder.com/app/recs")

time.sleep(1)

# ------------------------------- User Data --------------------------------------------- #
fb_data = {
    # "email": "l**********s@gmail.com",
    # "password": "senha"
}

# ------------------------------- Get to Login --------------------------------------------- #
login = driver.find_element(By.XPATH, '//*[@id="o41285377"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()

time.sleep(1)

# ------------------------------- Login Process --------------------------------------------- #
fb = driver.find_element(By.XPATH, '//*[@id="o-1687095699"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb.click()

time.sleep(1)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email = driver.find_element(By.NAME, "email")
email.send_keys(fb_data["email"])

password = driver.find_element(By.NAME, "pass")
password.send_keys(fb_data["password"])
password.send_keys(Keys.ENTER)


driver.switch_to.window(base_window)

time.sleep(10)

# ------------------------------- Like process --------------------------------------------- #
allow_location = driver.find_element(By.XPATH, "//*[@id='o-1687095699']/div/div/div/div/div[3]/button[1]")
allow_location.click()

disallow_notification = driver.find_element(By.XPATH, "//*[@id='o-1687095699']/div/div/div/div/div[3]/button[2]")
disallow_notification.click()

cookies = driver.find_element(By.XPATH, "//*[@id='o41285377']/div/div[2]/div/div/div[1]/button")
cookies.click()

time.sleep(10)

dislike = driver.find_element(By.XPATH, "//*[@data-testid='gamepadDislike']")
like = driver.find_element(By.XPATH, "//*[@data-testid='gamepadLike']")

for _ in range(5):
    dislike.click()

    time.sleep(1)





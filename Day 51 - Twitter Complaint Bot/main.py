from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

twitter_data = {
    # "username": "k**********z",
    # "password": "senha"
}


class InternetSpeedTwitterBot:
    def __init__(self):
        self.download = None
        self.upload = None

        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        sleep(2)

        run_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button .js-start-test")
        run_button.click()

        sleep(80)

        self.download = self.driver.find_element(By.CSS_SELECTOR, ".result-item-container-align-center .result-data-value").text
        self.upload = self.driver.find_element(By.CSS_SELECTOR, ".result-item-container-align-left .result-data-value").text

        sleep(1)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home?lang=en")

        sleep(2)

        user = self.driver.find_element(By.NAME, "text")
        user.send_keys(twitter_data["username"])

        next_step = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]')
        next_step.click()

        sleep(1)

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(twitter_data["password"])
        password.send_keys(Keys.ENTER)

        sleep(2)

        tweet = self.driver.find_element(By.CSS_SELECTOR, ".DraftEditor-editorContainer .public-DraftStyleDefault-block")
        tweet.send_keys(f"Hey He-Net, What is going on? My internet is only at {self.download}mbps for download and {self.upload}mbps for upload")

        sleep(0.5)

        send = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        # send.click()   take out of comment to send tweet


internet = InternetSpeedTwitterBot()

internet.get_internet_speed()

internet.tweet_at_provider()

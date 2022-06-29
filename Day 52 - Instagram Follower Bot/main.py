from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

account = "account you are searching for"

instagram_data = {
    "username": "your data",
    "password": "your data"
}


class InstaFollower:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("https://www.instagram.com/")

        sleep(1)

    def login(self):
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys(instagram_data["username"])

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(instagram_data["password"])

        sleep(1)

        password.send_keys(Keys.ENTER)

        sleep(5)

    def find_followers(self):
        search = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(account)

        sleep(3)

        search.send_keys(Keys.ENTER)
        search.send_keys(Keys.ENTER)

        sleep(2)

        # followers = self.driver.find_element(By.XPATH, f"//a[@href='/{account}/followers/']")
        following = self.driver.find_element(By.XPATH, f"//a[@href='/{account}/following/']")

        following.click()

        sleep(3)

    def follow(self):
        still_has_followers = True
        index = -1
        last_button = None

        while still_has_followers:
            all_buttons = self.driver.find_elements(By.CSS_SELECTOR, f"ul li button")

            follow_buttons = all_buttons[index+1:]
            print("next page")

            for button in follow_buttons:
                if button.text == "Seguir":
                    button.click()

                last_button = button

                sleep(0.5)

            print("done following")
            sleep(2)

            index = all_buttons.index(last_button)
            print(index)
            last_button.send_keys(Keys.END)

            sleep(3)


instagram = InstaFollower()
instagram.login()
instagram.find_followers()
instagram.follow()






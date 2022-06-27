from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C3&f_JT=P%2CI&f_WT=2&keywords=python&sortBy=R")

time.sleep(1)

# ------------------------------- User Data --------------------------------------------- #
login_data = {
    # "email": "lf********s@gmail.com",
    # "password": "senha"
}

# ------------------------------- Get to Login page --------------------------------------------- #
try:
    login_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
except:
    login_button = driver.find_element(By.XPATH, "/html/body/div/main/div/form/section/p[2]/button")
finally:
    login_button.click()

time.sleep(1)

# ------------------------------- Account Login --------------------------------------------- #
email_input = driver.find_element(By.NAME, "session_key")
email_input.send_keys(login_data["email"])

password_input = driver.find_element(By.NAME, "session_password")
password_input.send_keys(login_data["password"])

password_input.send_keys(Keys.ENTER)

time.sleep(0.5)

# ------------------------------- Save Job applications --------------------------------------------- #
scroll = driver.find_element(By.CSS_SELECTOR, ".jobs-search-results__list .job-card-list__title")
scroll.send_keys(Keys.PAGE_DOWN)
scroll.send_keys(Keys.PAGE_DOWN)
scroll.send_keys(Keys.PAGE_DOWN)
scroll.send_keys(Keys.PAGE_DOWN)

time.sleep(0.5)

jobs_list = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list .job-card-list__title")

print(len(jobs_list))

# ------------------------------- Apply for Jobs --------------------------------------------- #
counter = 0  # test mode

for job in jobs_list:
    job.click()
    counter += 1  # test mode
    time.sleep(1)

    apply_now = driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/div/div/div/button")
    apply_now.click()

    time.sleep(0.5)

    send_application = driver.find_element(By.CSS_SELECTOR, "form .artdeco-button--primary")
    print(send_application.text)

    if send_application.text == "Enviar candidatura":
        cellphone = driver.find_element(By.CSS_SELECTOR, ".jobs-easy-apply-form-section__grouping .fb-single-line-text__input")
        cellphone.send_keys("7********6")

        print(f"application sent {counter}")  # test mode
        # send_application.click()  # test mode

    exit_application = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss")
    exit_application.click()

    time.sleep(1)

    discard = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar .artdeco-button--primary")
    discard.click()


# todo: delete the test mode. Might need to add a few steps for after sending the job application





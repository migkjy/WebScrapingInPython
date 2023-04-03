from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

load_dotenv()

my_username = os.getenv("TWITTER_USER")
my_password = os.getenv("TWITTER_PASS")
my_phone = os.getenv("TWITTER_PHONE")

web = "https://twitter.com/i/flow/login"
path = "/Users/frankandrade/Downloads/chromedriver"
service = Service(path)
driver = webdriver.Chrome(service=service)
driver.get(web)
driver.maximize_window()


# wait of 6 seconds to let the page load the content
time.sleep(6)  # this time might vary depending on your computer

# locating username and password inputs and sending text to the inputs
# username
username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@autocomplete ="username"]')))
username.send_keys(my_username)

# Clicking on "Next" button
next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@role="button"]//span[text()="다음"]')))
next_button.click()


# Wait for the new page to load and check if the "다음" button is still present
try:
    next_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@role="button"]//span[text()="다음"]')))
    # Code to execute if "다음" button is present

    # locating phone input and sending text to the input
    # phone
    phone = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@name ="text"]')))
    phone.send_keys(my_phone)

    # Clicking on "Next" button
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@role="button"]//span[text()="다음"]')))
    next_button.click()

    
except:
    # Code to execute if "다음" button is not present
    pass


# password
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@autocomplete ="current-password"]')))
password.send_keys(my_password)

# locating login button and then clicking on it, 언어설정도 고려할 것
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@role="button"]//span[text()="로그인하기"]')))
login_button.click()


# wait of 2 seconds after clicking button
time.sleep(2)

# closing driver
driver.quit()



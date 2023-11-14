from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

CHROME_PATH = os.environ.get("CHROME_PATH")

PARTY_SIZE = os.environ.get("PARTY_SIZE")
DATE = os.environ.get("DATE")
START_TIME = os.environ.get("START_TIME")
VENUE_ID = os.environ.get("VENUE_ID")

# Personal info
FIRST_NAME = os.environ.get("FIRST_NAME")
LAST_NAME = os.environ.get("LAST_NAME")
EMAIL = os.environ.get("EMAIL")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")

start_time = datetime.strptime(f"{DATE} {START_TIME}", "%Y-%m-%d %H:%M:%S")
print(start_time)

# initialize browser
service = Service()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
browser = webdriver.Chrome(service = service, options = chrome_options)

# wait time to be used for
wait = WebDriverWait(browser, 10)

# navigate to URL
URL = f"https://book.topgolf.com/#/?venue_id={VENUE_ID}&party_size={PARTY_SIZE}&date={DATE}"
browser.get(URL)

# generate list of times desired
formatted_time = start_time.strftime("%I:%M %p")
combined_times = [formatted_time]
for i in range(1, 13):
    delta = timedelta(minutes = 15 * i)
    combined_times.append((start_time + delta).strftime("%I:%M %p"))
    combined_times.append((start_time - delta).strftime("%I:%M %p"))

time.sleep(3)
time_items = browser.find_elements(by = By.CLASS_NAME, value= 'time')

# Looks to find desired time
for desired_time in combined_times:
    found_time = None
    for time_item in time_items:
        if desired_time == time_item.text:
            found_time = time_item
            found_time.click()
            break
    if found_time is not None:
        break

# reserve button
reserve_button = browser.find_element(by = By.XPATH, value = f"//b[text()='Reserve']")
reserve_button.click()

# Continue as a guest
continue_as_guest_button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@alt='Continue As Guest button']")))
continue_as_guest_button.click()

# full name button
full_name_button = wait.until(EC.presence_of_element_located((By.XPATH, "//p[text()='add full name']")))
full_name_button.click()

# first name input
first_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='input-31']")))
first_name_input.send_keys(FIRST_NAME)

# last name input
last_name_input = browser.find_element(by = By.XPATH, value = "//input[@id='input-33']")
last_name_input.send_keys(LAST_NAME)

# phone input
phone_input = browser.find_element(by = By.XPATH, value = "//input[@placeholder='Phone Number']")
phone_input.send_keys(PHONE_NUMBER)

# email input
email_input = browser.find_element(by = By.XPATH, value = "//input[@id='input-35']")
email_input.send_keys(EMAIL)

# update button
update_button = browser.find_element(by = By.XPATH, value = '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/footer/div/button')
update_button.click()

# checkboxes
check_1 = browser.find_element(by = By.XPATH, value = "//input[@id='checkbox-2']")
check_1.click()
check_2 = browser.find_element(by = By.XPATH, value = "//input[@id='checkbox-5']")
check_2.click()

# add credit card button
credit_card_button = browser.find_element(by = By.XPATH, value = '//*[@id="app"]/div/div[1]/main/div[2]/div/div/section[2]/div/div/div[1]/button')
credit_card_button.click()


input("Press enter to close browser...")

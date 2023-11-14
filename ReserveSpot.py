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

start_time = datetime.strptime(f"{DATE} {START_TIME}", "%Y-%m-%d %H:%M:%S")
print(start_time)

# initialize browser
service = Service()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
browser = webdriver.Chrome(service = service, options = chrome_options)

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



input("Press enter to close browser...")

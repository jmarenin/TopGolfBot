from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

CHROME_PATH = os.environ.get("CHROME_PATH")
URL = os.environ.get("TOP_GOLF_URL")


# initialize browser
service = Service()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
browser = webdriver.Chrome(service = service, options = chrome_options)

# navigate to URL
browser.get(URL)


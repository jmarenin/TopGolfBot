from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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

# select number of players
player_dropdown = browser.find_element(by = By.NAME, value = 'players')
select_players = Select(player_dropdown)
select_players.select_by_value("6")

input("Press enter to close browser...")
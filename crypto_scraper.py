from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime as dt


# Add the path to the chrome driver
CHROME_DRIVER_PATH = "./drivers/chromedriver"
coin = 'MANA'

url = f"https://wazirx.com/exchange/{coin}-USD"

browser = webdriver.Chrome(CHROME_DRIVER_PATH)
browser.get(url)

# CREATE A DELAY VARIABLE:
delay = 3 # this is in seconds, enough time for page to render

try: 
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'price-text')))
    print("Page is ready: ")

except TimeoutException as te:
    print(f"TimeoutException Raised: {te}")

def price_parser(driver):
    prices = [x.text for x in driver.find_elements_by_class_name('price-text')]
    tickers = [x.text for x in driver.find_elements_by_class_name('market-name-text')]
    ts = dt.now()

    to_db = {
        'tickers':tickers,
        'prices': prices, 
        'ts': ts
    }

    return to_db

if __name__ == '__main__':
    parsed_prices = price_parser(browser)
    
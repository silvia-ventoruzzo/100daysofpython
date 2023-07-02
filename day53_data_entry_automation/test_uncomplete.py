from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common import exceptions
from time import sleep

chrondriver_path = '../chromedriver_mac64/chromedriver'
service = Service(chrondriver_path)

FORM_URL = 'https://forms.gle/ByuVsbK1QDuhaF157'
ZILLOW_URL = 'https://www.zillow.com/homes/'

search_location = 'San Francisco'
listing_type = 'rent'
price_min = None
price_max = 3000
n_bedrooms = 1
n_baths = None

driver = webdriver.Chrome(service=service)

# 1. Go to Zillow
driver.get(ZILLOW_URL)
sleep(10)

# 2. Filter for city San Francisco
if search_location is not None:
    search_field = driver.find_element(By.XPATH, "//input[contains(@placeholder,'City, Neighborhood, ZIP, Address')]")
    search_field.send_keys(search_location)
    search_field.send_keys(Keys.ENTER)

# 3. Choose type of listing
type_button = driver.find_element(By.ID, 'listing-type')
type_button.click()
if listing_type.lower() == 'sale':
    type_option = driver.find_element(By.ID, "__c11n_59a205")
elif listing_type.lower() == 'rent':
    type_option = driver.find_element(By.ID, "isForRent")
else:
    raise ValueError('listing_type can either be sale, rent or skip')
type_option.click()
apply_button = driver.find_element(By.XPATH, "//button[contains(@data-test,'close-filters-button')]")
apply_button.click()

# 4. Choose price
if not (price_min is None and price_max is None):
    price_button = driver.find_element(By.XPATH, "//button[contains(@data-test,'price-filters-button')]")
    price_button.click()
    
    price_min = price_min if price_min is not None else 0
    min_field = driver.find_element(By.XPATH, "//input[contains(@data-test,'price-exposed-min')]")
    min_field.clear()
    min_field.send_keys(price_min)
    min_field.send_keys(Keys.ENTER)
        
    if price_max is not None:
        max_field = driver.find_element(By.XPATH, "//input[contains(@data-test,'price-exposed-max')]")
        max_field.clear()
        max_field.send_keys(price_max)
        max_field.send_keys(Keys.ENTER)      
    else:
        apply_button.click()

# 5. Choose number of bedrooms and bathrooms

driver.quit()
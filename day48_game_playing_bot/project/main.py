from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrondriver_path = '../chromedriver_mac64/chromedriver'
service = Service(chrondriver_path)
driver = webdriver.Chrome(service=service)
url = 'http://orteil.dashnet.org/experiments/cookie/'
driver.get(url)

# Click on cookie
cookie = driver.find_element(By.ID, "cookie")

click_wait_time = time.time() + 5
end_of_game_time = time.time() + 60*5

while True:
    cookie.click()
    
    # Every 5 seconds:
    if time.time() > click_wait_time:

        # Available ones have class="", while non available ones have class="grayed"
        add_ons = driver.find_elements(By.CSS_SELECTOR, '#store [class=""]')
        available_add_ons_ids = [element.get_attribute("id") for element in add_ons]

        # Get price
        prices = []
        for id in available_add_ons_ids:
            price = driver.find_element(By.CSS_SELECTOR, f'#{id} b')
            prices.append(int(''.join(filter(str.isdigit, price.text))))

        if len(prices) > 0:
            max_price = prices.index(max(prices))
            add_on_to_buy_id = available_add_ons_ids[max_price]
            add_on_to_buy = driver.find_element(By.ID, add_on_to_buy_id)
            add_on_to_buy.click()

# After 5 minutes stop the bot and check the cookies per second
    if time.time() > end_of_game_time:
        # Get cookies per second value
        cps = driver.find_element(By.ID, "cps")
        # cps = float(cps.text.split(':')[1].strip())
        print(cps.text)
        break

driver.quit()
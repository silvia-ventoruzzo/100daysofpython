from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrondriver_path = '../chromedriver_mac64/chromedriver'
service = Service(chrondriver_path)
driver = webdriver.Chrome(service=service)
url = 'https://www.python.org/'
driver.get(url)

dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
dates = [d.get_attribute("datetime").split('T')[0] for d in dates]

events = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")
events = [e.get_attribute("text") for e in events]

driver.quit()

upcoming_events = {}
for n in range(len(dates)):
    upcoming_events[n] = {
        'date':dates[n],
        'name':events[n]
    }
print(upcoming_events)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrondriver_path = '../chromedriver_mac64/chromedriver'
service = Service(chrondriver_path)
driver = webdriver.Chrome(service=service)
url = 'https://en.wikipedia.org/wiki/Main_Page'
driver.get(url)

article_count = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]')
article_count = int(article_count.text.replace(',', ''))
print(article_count)

driver.quit()


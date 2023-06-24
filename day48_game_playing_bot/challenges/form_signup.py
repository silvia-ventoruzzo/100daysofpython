from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrondriver_path = '../chromedriver_mac64/chromedriver'
service = Service(chrondriver_path)
driver = webdriver.Chrome(service=service)
url = 'http://secure-retreat-92358.herokuapp.com/'
driver.get(url)

# Fill form elements
first_name = driver.find_element(By.NAME, "fName")
first_name.clear()
first_name.send_keys("Silvia")

last_name = driver.find_element(By.NAME, "lName")
last_name.clear()
last_name.send_keys("V")

first_name = driver.find_element(By.NAME, "email")
first_name.clear()
first_name.send_keys("silvia@nomyrealemail.com")

# Click sign up button
signup_button = driver.find_element(By.CLASS_NAME, "btn-primary")
signup_button.click()

driver.quit()
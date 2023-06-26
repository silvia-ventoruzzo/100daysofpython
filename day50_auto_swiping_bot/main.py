import os
from dotenv import load_dotenv
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from time import sleep

load_dotenv(dotenv_path=Path('./twilio.env'))
OWN_PHONE_NUMBER = os.getenv('OWN_PHONE_NUMBER')

chrondriver_path = '../chromedriver_mac64/chromedriver'
service = Service(chrondriver_path)
driver = webdriver.Chrome(service=service)

# Go to website
url = 'https://tinder.com/'
driver.get(url)

# Login using phone number
login_button = driver.find_element(By.XPATH, '//*[@id="q-971264251"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()
using_phone_number_button = driver.find_element(By.XPATH, '//*[@id="q1595321969"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button/div[2]/div[2]/div/div')
using_phone_number_button.click()
# This method requests a verification that doesn't work through bot, however I don't want to use facebook
# I will therefore doing it manually (it defeats the purpose, but it be like that sometimes)
# verify_button = driver.find_element(By.ID, "home_children_button")
country_code = OWN_PHONE_NUMBER[:3]
phone_number = OWN_PHONE_NUMBER[3:]
country_field = driver.find_element(By.XPATH, '//*[@id="q1595321969"]/main/div/div[1]/div/div[2]/div/div[1]/div/div[2]')
country_field.send_keys(country_code)
number_field = driver.find_element(By.NAME, "phone_number")
number_field.send_keys(phone_number)
continue_button = driver.find_element(By.XPATH, '//*[@id="q1595321969"]/main/div/div[1]/div/div[3]/button/div[2]/div[2]')
continue_button.click()
# This authentification method is not possible to automate as it requests phone and email reference codes
allow_button = driver.find_element(By.XPATH, '//*[@id="q1595321969"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
allow_button.click()

# Automatically swipe left
negative_button = driver.find_element(By.XPATH, '//*[@id="q-971264251"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[2]/button')
negative_button.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    if name.lower() != 'guyyouwant':
        print("called")
        try:
            negative_button = driver.find_element(By.XPATH, '//*[@id="q-971264251"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[2]/button')
            negative_button.click()
        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except exceptions.NoSuchElementException:
                sleep(2)   
    
    else:
        try:
            positive_button = driver.find_element(By.XPATH, '//*[@id="q-971264251"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button')
            positive_button.click()
        
        #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
        except exceptions.ElementClickInterceptedException:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

    name = driver.find_element(By.XPATH, "//span[contains(@itemprop, 'name')]") 
    name = name.text # For whatever reason, this is the name of the person that follows
    
    
driver.quit()


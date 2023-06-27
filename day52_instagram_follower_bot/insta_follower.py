from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from time import sleep

chrondriver_path = '../chromedriver_mac64/chromedriver'
service = Service(chrondriver_path)

URL = 'https://www.instagram.com'

class InstaFollower:
    
    def __init__(self, username, password, account):
        self.driver = webdriver.Chrome(service=service)
        self.username = username
        self.password = password
        self.account = account
    
    def login(self):
        login_url = f"{URL}/accounts/login/"
        self.driver.get(login_url)
        sleep(10)

        # 1. Reject cookies
        reject_cookies_button = self.driver.find_element(By.CLASS_NAME, "_a9_1")
        reject_cookies_button.click()
        sleep(10)

        # 2. Input username and password
        username_field = self.driver.find_element(By.NAME, "username")
        username_field.send_keys(self.username)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(self.password)
        login_button = self.driver.find_element(By.XPATH, "//button[contains(@type,'submit')]")
        login_button.click()
        sleep(10) # While it loads page

        # 3. Reject notifications
        reject_notification_button = self.driver.find_element(By.CLASS_NAME, "_a9_1")
        reject_notification_button.click()
    
    def find_followers(self):
        # 1. Go to account page and get followers number
        account_url = f"{URL}/{self.account}"
        self.driver.get(account_url)
        sleep(5)
        followers_count = self.driver.find_element(By.XPATH, 
                                            '//*[@id="mount_0_0_PZ"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/ul/li[2]/a/span/span')
        followers_count = int(followers_count.text)

        # 2. Go to account page
        followers_url = f"{account_url}/followers/"
        self.driver.get(followers_url)
        sleep(5)

        # 3. Scroll followers list
        pop_up = self.driver.find_element(By.CLASS_NAME, "_aano")
        follow_buttons = self.driver.find_elements(By.CLASS_NAME, "_acas")
        # Stop scrolling when there are no more followers
        while len(follow_buttons) < followers_count: 
            print(len(follow_buttons))
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', pop_up)
            sleep(5)
            follow_buttons = self.driver.find_elements(By.CLASS_NAME, "_acas")
        self.follow_buttons = follow_buttons
    
    def follow(self):
        # 1. Find follow buttons
        for button in self.follow_buttons:
            sleep(2)
            try:
                button.click()
            except exceptions.ElementClickInterceptedException:
                # If you already follow an account, it'll ask whether you want to unfollow
                # In this case click on Cancel
                cancel_button = self.driver.find_element(By.CLASS_NAME, "_a9_1")
                cancel_button.click()
                
    def quit_driver(self):
        self.driver.quit()
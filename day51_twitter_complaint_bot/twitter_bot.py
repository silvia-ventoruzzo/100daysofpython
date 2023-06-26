from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

chrondriver_path = '../chromedriver_mac64/chromedriver'
service = Service(chrondriver_path)

SPEEDTEST_URL = 'https://www.speedtest.net/'
TWITTER_URL = 'https://twitter.com/'

class InternetSpeedTwitterBot:
    
    def __init__(self, download_speed, upload_speed, twitter_username, twitter_password):
        self.driver = webdriver.Chrome(service=service)
        self.expected_down = download_speed
        self.expected_up = upload_speed
        self.username = twitter_username
        self.password = twitter_password
        
    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        # 1. Need to accept cookies
        cookie_accept_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookie_accept_button.click()

        # 2. Start test
        start_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        start_button.click()
        
        # 3. Wait
        waiting = True
        while waiting:
            sleep(10)
            # 4. Pop up to click on "Back to test results"
            close_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')
            if close_button.is_displayed():
                close_button.click()
                waiting = False

        # Get speed info
        actual_down = self.driver.find_element(By.CLASS_NAME, "download-speed")
        self.actual_down = float(actual_down.text)
        actual_up = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        self.actual_up = float(actual_up.text)
        
        print(self.actual_down)
        print(self.actual_up)
        
    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        sleep(5)
        
        # 1. Login
        login_button = self.driver.find_element(By.XPATH, "//a[contains(@href,'/login')]")
        login_button.click()
        sleep(5)

        # 2. Insert username
        username_field = self.driver.find_element(By.XPATH, "//input[contains(@autocomplete,'username')]")
        username_field.send_keys(self.username)
        forward_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        forward_button.click()
        sleep(5)

        # 3. Insert password
        password_field = self.driver.find_element(By.XPATH, "//input[contains(@autocomplete,'current-password')]")
        password_field.send_keys(self.password)
        final_login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        final_login_button.click()
        sleep(5)

        # 4. Create Tweet
        tweet_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div')
        tweet_text = f'TEST: Why is my internet speed {self.actual_down}down/{self.actual_up}up when I pay for {self.expected_down}down/{self.expected_up}up?'
        tweet_field.send_keys(tweet_text)
        sleep(5)

        # 5. Send Tweet
        publish_button = self.driver.find_element(By.XPATH, "//div[contains(@data-testid,'tweetButtonInline')]")
        publish_button.click()
        
        print('Tweet sent')
        
    def quit_driver(self):
        self.driver.quit()
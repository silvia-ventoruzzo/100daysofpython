import os
from dotenv import load_dotenv
from pathlib import Path
from time import sleep

from day52_instagram_follower_bot.insta_follower import InstaFollower

load_dotenv(dotenv_path=Path('./twilio.env'))
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

account = 'londonappbrewery'

bot = InstaFollower(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, account)
bot.login()
sleep(10)
bot.find_followers()
bot.follow()
bot.quit_driver()

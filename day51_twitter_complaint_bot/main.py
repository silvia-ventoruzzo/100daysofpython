import os
from dotenv import load_dotenv
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from time import sleep

from day51_twitter_complaint_bot.twitter_bot import InternetSpeedTwitterBot

load_dotenv(dotenv_path=Path('./twilio.env'))
TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')

PROMISED_DOWN = 300
PROMISED_UP = 50

bot = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP, TWITTER_USERNAME, TWITTER_PASSWORD)
bot.get_internet_speed()

if bot.actual_down < bot.expected_down or bot.actual_up < bot.expected_up:
    bot.tweet_at_provider()

bot.quit_driver()
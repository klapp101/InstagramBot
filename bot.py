from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random
import pandas as pd

# Enter the credentials of your Instagram account
ig_username = 'username_here'
ig_password = 'password_here'

# List of usernames to message

# usernames = pd.read_csv('vendors.csv')
# usernames = usernames['Instagram ']
usernames = ['username_here','username_here']

# List of messages to send

messages = pd.read_csv('messages.csv')
messages = messages['Messages']

# Delay time between messages in sec:
between_messages = 2000

browser = webdriver.Chrome('/Users/ryanklapper/Desktop/Projects_2022/InstagramBot/chromedriver')

# Authorization:
def auth(username, password):
    try:
        browser.get('https://instagram.com')
        time.sleep(random.randrange(2,4))

        input_username = browser.find_element_by_name('username')
        input_password = browser.find_element_by_name('password')

        input_username.send_keys(username)
        time.sleep(random.randrange(1,2))
        input_password.send_keys(password)
        time.sleep(random.randrange(1,2))
        input_password.send_keys(Keys.ENTER)

    except Exception as err:
        print(err)
        browser.quit()

# Sending messages:
def send_message(users, messages):
    try:
        browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        time.sleep(random.randrange(3,5))
        browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        time.sleep(random.randrange(1,2))
        browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click()
        for user in users:
            time.sleep(random.randrange(1,2))
            browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
            time.sleep(random.randrange(2,3))
            browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]').find_element_by_tag_name('button').click()
            time.sleep(random.randrange(3,4))
            browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
            time.sleep(random.randrange(3,4))
            text_area = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
            text_area.send_keys(random.choice(messages))
            time.sleep(random.randrange(2,4))
            text_area.send_keys(Keys.ENTER)
            print(f'Message successfully sent to {user}')
            time.sleep(between_messages)
            browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()

    except Exception as err:
        print(err)
        time.sleep(5)
        browser.quit()


auth(ig_username, ig_password)
time.sleep(random.randrange(2,4))
send_message(usernames, messages)



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
 
driver = webdriver.Firefox()
driver.get('https://www.twitter.com/')
print("Opened twitter...")
login = driver.find_element_by_xpath("//*[@class='Button StreamsLogin js-login']")
login.click()
email = driver.find_element_by_xpath("//*[@class='text-input email-input js-signin-email']")
email.send_keys('Enter your email address here')
print("Email Id entered...")
password = driver.find_element_by_xpath("//*[@name='session[password]']")
password.send_keys('Enter your password is here')
print("Password entered...")
button = driver.find_element_by_xpath("//*[@class='submit btn primary-btn js-submit']")
button.click()
driver.find_element_by_xpath("//div[@id='tweet-box-home-timeline']").send_keys("Bot is tweeting here");
tweetbutton = driver.find_element_by_xpath("//*[@class='btn primary-btn tweet-action tweet-btn js-tweet-btn']")
tweetbutton.click()
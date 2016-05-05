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
#login = driver.find_element_by_class('email')
login.click()
email = driver.find_element_by_xpath("//*[@class='text-input email-input js-signin-email']")
email.send_keys('nter your email address her')
print("Email Id entered...")
password = driver.find_element_by_xpath("//*[@name='session[password]']")
password.send_keys('Enter your password here')
print("Password entered...")
button = driver.find_element_by_xpath("//*[@class='submit btn primary-btn js-submit']")
button.click()
driver.find_element_by_xpath("//div[@id='tweet-box-home-timeline']").send_keys("Bot is tweeting here");
tweetbutton = driver.find_element_by_xpath("//*[@class='btn primary-btn tweet-action tweet-btn js-tweet-btn']")
tweetbutton.click()
'''
driver.get("https://www.facebook.com/apoorvu")
post_box=driver.find_element_by_xpath("//*[@name='xhpc_message']")
post_box.click()
post_box.send_keys("Testing using Name not ID.Selenium is easy.")
sleep(2)
post_it=driver.find_element_by_xpath("//*[@id='u_0_1a']/div/div[6]/div/ul/li[2]/button")
post_it.click()
print("Posted...")
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
 
driver = webdriver.Firefox()
driver.get('https://www.facebook.com/')
print("Opened facebook...")
time.sleep(2)
email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")
email.send_keys('achinsagar@gmail.com')
print("Email Id entered...")
password = driver.find_element_by_xpath("//input[@id='pass']")
password.send_keys('19indep47')
print("Password entered...")
button = driver.find_element_by_xpath("//input[@id='u_0_w']")
button.click()
time.sleep(2)
statusbox = driver.find_element_by_xpath("//textarea[@class='uiTextareaAutogrow _3en1']")
statusbox.send_keys("Bot is typing here");
postbutton = driver.find_element_by_xpath("//*[text()='Post']")
postbutton.click()
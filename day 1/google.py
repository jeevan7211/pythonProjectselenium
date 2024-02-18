
import os
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
print("sample test case started")


chromedriver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"

driver = webdriver.Chrome(chromedriver)
#driver=webdriver.firefox()
#driver=webdriver.ie()
#maximize the window size
driver.maximize_window()
#navigate to the url
driver.get("https://www.google.com/")
#identify the Google search text box and enter the value
driver.find_element(By.NAME, "q").send_keys("javatpoint")

time.sleep(3)
#click on the Google search button
#driver.find_element("name","btnK").send_keys(Keys.ARROW_DOWN)
#driver.find_element("name","btnK").send_keys(Keys.ARROW_DOWN)
driver.find_element("name","btnK").send_keys(Keys.ENTER)
time.sleep(3)
#close the browser
driver.close()
print("sample test case successfully completed")
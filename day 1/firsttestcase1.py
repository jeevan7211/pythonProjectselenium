from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
try:
    element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.NAME, "username").send_keys("Admin"))


    )

finally:
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CLASS_NAME, "oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()

# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.find_element(By.NAME, "username").clear()
# driver.find_element(By.NAME, "username").click()
# driver.find_element(By.NAME, "username").send_keys("Admin")
# driver.find_element(By.NAME, "password").click()
# driver.find_element(By.NAME, "password").send_keys("admin123")
# driver.find_element(By.CLASS_NAME, "oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

# Directly set username and password for testing (remove in production)
USERNAME = '0862428967'
PASSWORD = os.getenv('PASSWORD', 'Governtooling137')
print(USERNAME)

if USERNAME is None or PASSWORD is None:
    raise ValueError("Environment variables USERNAME and PASSWORD must be set")

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/")

# Wait for the cookies prompt and click "Decline optional cookies"
cookies_button = WebDriverWait(driver, timeout=30).until(
    lambda d: d.find_element(By.XPATH, '//button[text()="Decline optional cookies"]'))
cookies_button.click()

# Find username input area and write username
username = WebDriverWait(driver, timeout=60).until(
    lambda d: d.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))
username.send_keys(USERNAME)
 
# Find password input area and write password
password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys(PASSWORD)

# Click on Login Button
enter = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
enter.click()
time.sleep(15)

# Click on Not Now in pop up
not_now = driver.find_element(By.CSS_SELECTOR, '._a9_1')
not_now.click()
time.sleep(60)
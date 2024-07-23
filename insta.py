from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Directly set username and password for testing (remove in production)
USERNAME = ''
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
time.sleep(5)

# Click on Not Now in the first pop up
not_now = WebDriverWait(driver, timeout=30).until(
    EC.element_to_be_clickable((By.XPATH, '//div[text()="Not now" and @role="button"]')))
not_now.click()

# Click on Not Now in the second pop up
not_now = driver.find_element(By.CSS_SELECTOR, '._a9_1')
not_now.click()
time.sleep(5)

# Click on the "Create" button in the left sidebar
create_button = WebDriverWait(driver, timeout=30).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.x9f619.xxk0z11.xii2z7h.x11xpdln.x19c4wfv.xvy4d1p')))
create_button.click()

# Wait for the dropdown to be visible and print its HTML for verification
dropdown_element = WebDriverWait(driver, timeout=30).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.x9f619.xxk0z11.xii2z7h.x11xpdln.x19c4wfv.xvy4d1p')))

# Print the HTML of the dropdown for debugging
print(dropdown_element.get_attribute('innerHTML'))

# Interact with elements in the dropdown if needed
# Example: click on the first element in the dropdown
try:
    first_element = dropdown_element.find_element(By.XPATH, './/a[0]')
    first_element.click()
except Exception as e:
    print(f"An error occurred: {e}")

# Wait for further instructions or perform next steps
time.sleep(60)

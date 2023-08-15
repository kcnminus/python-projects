from selenium import webdriver
import time

try:
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get('https://umbrella.policygenius.com')
  time.sleep(10)

  search_button = driver.find_element('xpath', '//button[text()="Sign In"]')
except Exception as e:
    print(f"Error: {e}")
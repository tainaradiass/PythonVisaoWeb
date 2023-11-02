from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/js/default.asp")
import time
time.sleep(5)
driver.quit()
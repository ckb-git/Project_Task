from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
# ser_obj = Service("path of chrome exe file")
# driver= webdriver.Chrome(ser_obj)
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome()
driver.get("https://www.google.co.in/")
# m = driver.find_element_by_name("q")
m = driver.find_element(By.NAME,"q")
m.send_keys("Chandan")
m.send_keys(Keys.ENTER)
time.sleep(5)

driver.quit()

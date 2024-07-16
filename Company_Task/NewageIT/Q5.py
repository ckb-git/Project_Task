from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.myntra.com/")
search = driver.find_element(By.XPATH, "//input[@class='desktop-searchBar']")
search.send_keys("plant")
search.send_keys(Keys.RETURN)
time.sleep(5)

item7th = driver.find_elements(By.CLASS_NAME, "product-brand")[6]
item7th.click()
time.sleep(5)

addcart = driver.find_element(By.XPATH, "//button[contains(@class, 'add-to-bag')]")
addcart.click()
time.sleep(5)

cart = driver.find_element(By.CLASS_NAME, "desktop-cart")
cart.click()

itemremove= driver.find_element(By.XPATH, "//button[contains(@class, 'item-remove')]")
itemremove.click()

driver.quit()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver= webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("error_user");
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce");
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
time.sleep(2)

if(driver.find_element(By.XPATH,"//div[@class='app_logo']").is_displayed()):
    print ("login Successfully")
else:
    print("login Unsuccessfully")

proName = driver.find_element(By.XPATH,"//a[@id='item_4_title_link'] ").text
proPrice = driver.find_elements(By.XPATH,"//div[@class='inventory_item_price']")
price1=proPrice[0].text
print()
print("product_name: "+proName)
print("product_price: "+price1)


button = driver.find_elements(By.XPATH,"//button[@class='btn btn_primary btn_small btn_inventory ']")
button[0].click()
time.sleep(2)

driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
time.sleep(5)

cart_proName = driver.find_element(By.XPATH,"//a[@id='item_4_title_link'] ").text
cart_proPrice = driver.find_elements(By.XPATH,"//div[@class='inventory_item_price']")
price2=cart_proPrice[0].text
print()
print("Cart product_name: "+cart_proName)
print("Cart product_price: "+price2)

print()
if(proName==cart_proName and price1==price2):
    print("validated")
else:
    print("not validated")
driver.quit()


# //a[@class='shopping_cart_link']




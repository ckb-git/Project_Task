from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import json

driver = webdriver.Chrome()


# Navigate to the Gmail login page
driver.get("http://gmail.com")
driver.maximize_window()

# Find the email input field and enter the username
email_input = driver.find_element(By.XPATH,"//input[@id='identifierId']")
email_input.send_keys("abc@gmail.com")
email_input.send_keys(Keys.ENTER)
time.sleep(5)

# Wait for the password input field to load
password_input = driver.find_element(By.XPATH, "//input[@name='password']")
password_input.send_keys("1234")
password_input.send_keys(Keys.ENTER)
time.sleep(5)

# Find and click the "Inbox" link to go to the inbox
inbox_link = driver.find_element(By.XPATH,"//div[@class='TN bzz aHS-bnt']//div[@class='aio UKr6le']")
inbox_link.click()
time.sleep(3)

# Find all the email  in the inbox
emails= driver.find_elements(By.XPATH,"//span[@class='yP']")

# Extract the top ten email subjects
Top_ten_emails = [i.text for i in emails[:10]]

# prints emails
print("Top Ten Emails:")
for i, email in enumerate(Top_ten_emails, 1):
    print(f"{i}. {email}")

# Save the top ten emails to a JSON file
with open("Top_ten_emails.json", "w") as json_file:
    json.dump(Top_ten_emails, json_file)

# Close the browser window
driver.quit()

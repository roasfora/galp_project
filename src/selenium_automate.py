import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open webpage
driver.get("http://localhost:8000/index.html")

# Add delay to see page load
time.sleep(2)

# Fill in the form with delays
name_field = driver.find_element(By.XPATH, "//input[@placeholder='Inserir nome']")
name_field.send_keys("John Doe")
time.sleep(2)  # Pause to see the name being typed

email_field = driver.find_element(By.XPATH, "//input[@placeholder='Inserir email']")
email_field.send_keys("john.doe@example.com")
time.sleep(2)  # Pause to see the email being typed

message_field = driver.find_element(By.XPATH, "//textarea[@placeholder='Inserir mensagem']")
message_field.send_keys("Estou interessado no curso de DataOps!")
time.sleep(2)  # Pause to see the message being typed

# Submit the form (if there is a button)
submit_button = driver.find_element(By.TAG_NAME, "button")
submit_button.click()

print("Form Submitted!")

# Wait before closing to see the submission
time.sleep(3)

# Close the browser
driver.quit()

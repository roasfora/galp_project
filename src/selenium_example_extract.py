from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("http://localhost:8000/index.html")  # Replace with your actual URL

# Extract course title
title_element = driver.find_element(By.TAG_NAME, "h1")
print(f"Course Title: {title_element.text}")

# Extract all paragraphs
paragraphs = driver.find_elements(By.TAG_NAME, "p")
for p in paragraphs:
    print(f"Paragraph: {p.text}")

# Close the browser
driver.quit()

# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Initialize WebDriver and open python.org
driver = webdriver.Chrome()
driver.get("https://www.python.org/")

# Maximize the browser window
driver.maximize_window()

# Generate a JavaScript alert
driver.execute_script("alert('This is the first alert!')")
time.sleep(2)

# Switch to the alert and accept it
alert = driver.switch_to.alert
print("Alert Text:", alert.text)  # Get and print alert text
alert.accept()
print("First alert accepted!")

# Generate a second JavaScript alert
driver.execute_script("alert('This is the second alert!')")
time.sleep(2)

# Dismiss the alert
alert = driver.switch_to.alert
print("Alert Text:", alert.text)
alert.dismiss()
print("Second alert dismissed!")

# Generate a third JavaScript prompt alert
driver.execute_script("var userInput = prompt('Enter your name:','Default');")
time.sleep(2)

# Send text to the prompt alert
alert = driver.switch_to.alert
print("Prompt Alert Text:", alert.text)
alert.send_keys("PythonUser")
alert.accept()
print("Prompt alert accepted with input!")

# Generate a confirmation alert
driver.execute_script("confirm('Are you sure you want to continue?')")
time.sleep(2)

# Switch to the confirmation alert and dismiss
alert = driver.switch_to.alert
print("Confirmation Alert Text:", alert.text)
alert.dismiss()
print("Confirmation alert dismissed!")

# Wait for 3 seconds before closing the browser
time.sleep(3)
driver.quit()

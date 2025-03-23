import os
from selenium import webdriver

# Define path to save the screenshot
screenshot_path = os.path.join("C:\\Users\\dhinesh\\Downloads", "google_screenshot.png")

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Capture and save screenshot in specified path
driver.save_screenshot(screenshot_path)

print(f"✅ Screenshot saved at: {screenshot_path}")

# Close the browser
driver.quit()

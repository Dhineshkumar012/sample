import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open first window (Google)
driver.get("https://www.google.com")
print("✅ Google window opened successfully!")

# Open a new window (W3Schools) using JavaScript
driver.execute_script("window.open('https://www.w3schools.com', '_blank');")
time.sleep(2)

# Switch to the second window
windows = driver.window_handles
driver.switch_to.window(windows[1])
print("✅ Switched to W3Schools window!")

# Open another window (Python.org)
driver.execute_script("window.open('https://www.python.org', '_blank');")
time.sleep(2)

# Switch to the third window
windows = driver.window_handles
driver.switch_to.window(windows[2])
print("✅ Switched to Python.org window!")

# Loop through all windows and perform maximize and minimize actions
for window in windows:
    driver.switch_to.window(window)

    # Maximize the window
    driver.maximize_window()
    print(f"🟢 Maximized window: {driver.current_url}")
    time.sleep(2)

    # Minimize the window (using JavaScript as WebDriver doesn't support minimize natively)
    driver.minimize_window()
    print(f"🔵 Minimized window: {driver.current_url}")
    time.sleep(2)

# Switch back to the first window
driver.switch_to.window(windows[0])
print("✅ Switched back to Google window!")

# Close all windows
for window in windows:
    driver.switch_to.window(window)
    driver.close()
    print(f"❌ Closed window: {window}")

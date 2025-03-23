import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/dhinesh/eclipse-workspace/Sample/driver/chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.w3schools.com/bootstrap/bootstrap_dropdowns.asp')
time.sleep(2)

img1 = driver.find_element(By.XPATH, '//*[@id="menu1"]')
img1.click()
time.sleep(3)
img2 = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/ul/li[1]/a')
img2.click()
time.sleep(3)

driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.in/ref=nav_logo")
driver.maximize_window()

driver.back()
driver.forward()

driver.refresh()

driver.quit()

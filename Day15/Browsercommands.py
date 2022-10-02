import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH, '//a[contains(text(), "OrangeHRM, Inc")]').click()

time.sleep(10)

driver.close()

driver.quit()

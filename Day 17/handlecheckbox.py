import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

serv_obj = Service("D:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# 1. select specific checkbox
#driver.find_element(By.XPATH,"//input[@id='monday']").click()

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes)) #7

#Appraoch

for checkbox in checkboxes:
    checkbox.click()

#for i in range (len(checkboxes)):
#   checkboxes[i].click()

time.sleep(5)

for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

driver.close()
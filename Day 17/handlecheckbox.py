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
# driver.find_element(By.XPATH,"//input[@id='monday']").click()

# select all the checkboxes

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))  # 7

# 1) Appraoch 1
# for checkbox in checkboxes:
#     checkbox.click()

# 2) Appraoch 2
# #for i in range (len(checkboxes)):
# #   checkboxes[i].click()
#
# time.sleep(5)

# 3) select multiple checkboxes by choice

# for checkbox in checkboxes:
#     weekname = checkbox.get_attribute('id')
#     if weekname== 'monday' or weekname=='tuesday' or weekname=='wednesday':
#         checkbox.click()

# 4) select last 2 checkboxes
# for i in range(len(checkboxes) - 2, len(checkboxes)):
#     checkboxes[i].click()

#
#
# driver.close()

# 5) select first 2 checkboxesa
for i in range(len(checkboxes)):
    checkboxes[i].click()
    if i < 2:
        checkboxes[i].click()

for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

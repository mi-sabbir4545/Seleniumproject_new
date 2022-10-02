import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("D:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

# drpcountry_ele = driver.find_element(By.XPATH, "//select[@id='input-country']")
# drpcountry_ele = driver.find_element(By.XPATH, "//select[@id='input-country']")
# drpcountry = Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))

# slect option fro th edropdown
# drpcountry.select_by_visible_text("India")
# drpcountry.select_by_value("10")  # argentina
# drpcountry.select_by_index(13)  # australia

# capture total number of the options

# alloptions = drpcountry.options
# print("Total Number of options:", len(alloptions))

# for opt in alloptions:
#     print(opt.text)

# slect option from dropdown without built in method

# for opt in alloptions:
#     if opt.text == "India":
#         opt.click()
#         break

allOptions=driver.find_elements(By.XPATH, "//select[@id='input-country']/option")
print("Total number of options", len(allOptions))

# for opt in allOptions:
#     print(opt.text)

for opt in allOptions:
    if opt.text == "India":
        opt.click()
        break



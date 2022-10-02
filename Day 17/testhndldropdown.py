import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("D:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

alloption = driver.find_elements(By.XPATH, "//select[@id='speed']//option")
# print("All number of dropdown:", len(alloption))

# for opt in alloption:
#     print(opt.text)

for opt in alloption:
    if opt.text == "Slower":
        opt.click()
        break

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("admin")
# time.sleep(3)
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
time.sleep(5)
driver.find_element(By.XPATH, "//button[contains(text(), Login)]").click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test failed")

driver.close()



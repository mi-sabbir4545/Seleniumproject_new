import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Webdriver\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)

driver.find_element(By.XPATH, "//input[@name = 'txtUsername']").send_keys("admin")
driver.find_element(By.XPATH, "//input[@id='txtPassword']").send_keys("admin123")
driver.find_element(By.XPATH, "//input[@class='button']").click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
         print("Login Test Passed")
else:
     print("Login Test failed")

driver.close()

# driver.find_elements(By.XPATH, " ")

# driver.find_element(By.CLASS_NAME, "txtUsername").send_keys(admin)
# driver.find_elements(By.CLASS_NAME, " txtPassword").send_keys(admin123)
# driver.find_element_by_name("txtUsername").send_keys("admin")

# driver.find_element_by_id("txtPassword").send_keys("admin123")
# driver.find_element_by_id("btnLogin").click()
# act_title = driver.title
# exp_title = "OrangeHRM"
#
# if act_title == exp_title:
#         print("Login Test Passed")
# else:
#         print("Login Test failed")
#
#         driver.close()
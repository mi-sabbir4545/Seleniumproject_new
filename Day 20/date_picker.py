from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)  # switch to frame

# mm/dd/yyyy

# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("05/30/2022")

year = "2021"
month = "june"
date = "17"

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()  # opens datepiker

while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break;
    else:
        # driver.find_element(By.XPATH, "//a[@title='Next']").click()
        driver.find_element(By.XPATH, "//a[@title='Prev']").click()

# select date

time.sleep(3)
dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text == date:
        ele.click()
        break

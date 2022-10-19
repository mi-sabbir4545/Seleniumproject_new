import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
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
time.sleep(3)
driver.find_element(By.XPATH, "//button[contains(text(), Login)]").click()

time.sleep(5)
driver.find_element(By.XPATH, "//span[normalize-space()='My Info']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//a[normalize-space()='Personal Details']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='orangehrm-edit-employee-image']//img[@alt='profile picture']").click()

time.sleep(3)
# driver.find_element(By.XPATH, "//button[@class='oxd-icon-button employee-image-action']").click()
driver.find_element(By.XPATH, "//input[@type='file']").send_keys("D:\Images/my.jpg")

time.sleep(3)
details = driver.find_element(By.XPATH, "//a[normalize-space()='Personal Details']")
driver.execute_script("arguments[0].scrollIntoView();", details)

time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

time.sleep(3)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
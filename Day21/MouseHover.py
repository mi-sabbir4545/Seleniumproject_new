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
# admin = driver.find_element(By.XPATH, "(//span[contains(., 'Admin')])[1]")
driver.find_element(By.XPATH, "(//span[contains(., 'Admin')])[1]").click()
time.sleep(3)
# usermgmt = driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-chevron-down'])[1]")
driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-chevron-down'])[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(), 'Users')]").click()

# act = ActionChains(driver)

# act.move_to_element(admin).click().perform() #move_to_element(usermgmt).

act = ActionChains(driver)

time.sleep(2)
act.send_keys(Keys.TAB).perform()

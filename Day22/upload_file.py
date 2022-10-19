import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.monsterindia.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[@class='uprcse semi-bold']").click()
driver.find_element(By.XPATH, "(//input[@id='file-upload'])[1]").send_keys("D:\Images/file.pdf")



time.sleep(3)
driver.find_element(By.XPATH, "(//input[@class='btn disabled'])[1]").click()

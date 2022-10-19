import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demoqa.com/buttons")
driver.maximize_window()

button = driver.find_element(By.ID, "doubleClickBtn")

act = ActionChains(driver)

act.double_click(button).perform()

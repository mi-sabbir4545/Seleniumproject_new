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

button = driver.find_element(By.ID, "rightClickBtn")
act=ActionChains(driver)
act.context_click(button).perform()
time.sleep(1)
message = driver.find_element(By.XPATH, "//p[@id='rightClickMessage']")
print(message.text)
assert message.text == 'You have done a right click'

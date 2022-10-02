import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox=driver.find_element(By.NAME,'q')

searchbox.send_keys("Selenium")
searchbox.submit()

#time.sleep(5)

driver.find_element(By.XPATH,"//h3[normalize-space()='Selenium']").click()

#driver.quit()
#driver.close()
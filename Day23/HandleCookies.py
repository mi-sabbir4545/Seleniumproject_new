import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.nopcommerce.com/en/demo")
driver.maximize_window()

cookies = driver.get_cookies()
print("Size of Cookies: ", len(cookies))

for c in cookies:
    # print(c)
    print(c.get('name'),":",c.get('value'),":",c.get('expires'))

driver.quit()




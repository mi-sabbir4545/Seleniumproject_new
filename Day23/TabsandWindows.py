import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

serv_obj = Service("D:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)

# driver.get("https://www.nopcommerce.com/en/demo")
# driver.switch_to.new_window('tab')
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


# driver.get("https://www.nopcommerce.com/en/demo")
# driver.switch_to.new_window('window')
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
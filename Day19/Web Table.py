from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ops = webdriver.ChromeOptions()
ops.add_argument('--disable-notifications')

serv_obj = Service("D:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj, options=ops)

driver.get("https://whatmylocation.com/")
driver.maximize_window()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Webdriver\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.get("http://automationpractice.com/index.php")

driver.maximize_window()

sliders=driver.find_elements(By.CLASS_NAME, 'homeslider-container')
print(len(sliders)) #total number of home page

links=driver.find_elements(By.TAG_NAME,'a')
print(len(links)) #149 total number of links on home
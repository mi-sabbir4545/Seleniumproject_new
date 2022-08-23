from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Webdriver\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#id & name locators

#driver.find_element(By.ID,"small-searchterms").send_keys("Apple MacBook Pro 13-inch")
#driver.find_element(By.NAME,"q").send_keys("Apple MacBook Pro 13-inch")

# linktext & partial linktext

driver.find_element(By.LINK_TEXT,"Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Register").click()





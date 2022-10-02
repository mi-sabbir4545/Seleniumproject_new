import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# click on Link

#driver.find_element(By.LINK_TEXT, "Digital downloads").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()

#find number of
links = driver.find_elements(By.TAG_NAME,'a')
#links = driver.find_elements(By.XPATH,'//a')

print("Total Number of links:", len(links))

#print all the link names

for link in links:
    print(link.text)

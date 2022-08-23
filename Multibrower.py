from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "D:\\Webdriver\\chromedriver.exe")

driver.get("https://www.daraz.com.bd/")

print(driver.title)

driver.close()


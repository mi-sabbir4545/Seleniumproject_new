from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
time.sleep(5)

# driver.get("https://the-internet.herokuapp.com/basic_auth")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

driver.switch_to.frame("")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
driver.find_element(By.LINK_TEXT, "WebDriver").click()
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()

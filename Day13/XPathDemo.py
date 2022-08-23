from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

# Absulate Xpath
# driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-Shirts")
# driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()

# Relative xpath

# driver.find_element(By.XPATH, "//*[@id='search_query_top']").send_keys("T-Shirts")
# driver.find_element(By.XPATH, "//button[@name='submit_search']").click()

# or, and

# driver.find_element(By.XPATH, "//*[@id='search_query_top' or @placeholder= 'search']").send_keys("T-Shirts")
# driver.find_element(By.XPATH, "//button[@name='submit_search' and @class= 'btn btn-default button-search']").click()

# contains & start-with()

# driver.find_element(By.XPATH, "//input[contains(@id, 'search')]").send_keys("T-Shirts")
# driver.find_element(By.XPATH, "//button[starts-with(@name,'submit_')]").click()

driver.find_element(By.XPATH, "//a[test()='women']").click()

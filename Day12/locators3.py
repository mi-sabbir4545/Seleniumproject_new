from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Webdriver\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")

driver.maximize_window()

# tag & id combination

# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")

# tag & class

# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc@gmail.com")

# tag & attritube

# driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("sabbir")
# driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("sabbir")

# tag class & attrubute

driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("milon")

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# 1. Scroll down page by pixel
# driver.execute_script("window.scrollBy(0,3000)", "")
# value=driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved: ", value)

# 2. Scroll down till element is visible
# flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();", flag)
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved: ", value)  # 4951.81787109375

#3. Scroll down page till end

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved: ", value)

time.sleep(4)
# Scroll up to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved: ", value)

# driver.find_element(By.XPATH,"").click()
# driver.switch_to.alert.accept()
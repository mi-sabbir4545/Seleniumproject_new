from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path= "D:\Webdriver\chromedriver.exe")

driver.get("https://www.ushareit.com/")

print(driver.title)
print(driver.current_url)
time.sleep(3)

driver.find_elements(By.XPATH,"//*[@id='__layout'']/div/div[1]/div/div/div[1]/div[2]/div[1]").click()
#
# # driver.switch_to.default_content()
#
# driver.find_element_by_xpath("((//div[contains(text(), 'GROUP')])[1]").click()





from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# windowid = driver.current_window_handle
# print(windowid)

time.sleep(3)
driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
windowsIDs=driver.window_handles

#Approach1
# parentwindowid=windowsIDs[0] # CDwindow-0B4F4C4F2E1F16F04B813B1EFFA0CEFD
#
# childtwindowid=windowsIDs[1] # CDwindow-99B032E64E578F4D7B74EDFCE9350F14
#
# # print(parentwindowid,childtwindowid)
#
# driver.switch_to.window(childtwindowid)
# print("Title of the child window", driver.title)
#
# driver.switch_to.window(parentwindowid)
# print("Title of the parent window", driver.title)
#
# driver.close()


#Approach2

# for winid in windowsIDs:
#     driver.switch_to.window(winid)
#     print(driver.title)

time.sleep(3)

#close specific browser windows
for winid in windowsIDs:
    driver.switch_to.window(winid)
    if driver.title == "OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM":
        driver.close()

# if driver.title == "OrangeHRM" and driver.title == "XYZ":
# if driver.title == "OrangeHRM" or driver.title == "XYZ":


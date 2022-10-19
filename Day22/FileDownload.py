import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common.by import By
import os

location = os.getcwd()


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("D:\Webdriver\chromedriver.exe")

    # download files in desired location
    preferences = {"download.default_directory": location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(service=serv_obj)
    return driver


driver = chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()

file = driver.find_element(By.XPATH, "//a[normalize-space()='Microsoft Word official page']")
driver.execute_script("arguments[0].scrollIntoView();", file)

driver.find_element(By.XPATH,
                    "//body[1]/div[1]/main[1]/section[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[5]/a[1]").click()

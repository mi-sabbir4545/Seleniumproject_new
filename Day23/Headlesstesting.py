from selenium import webdriver


def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("D:\Webdriver\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    return driver


driver = headless_chrome()
driver.get("https://www.amazon.com/")
print(driver.title)
print(driver.current_url)
driver.close()

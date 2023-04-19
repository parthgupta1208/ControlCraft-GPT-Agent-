
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver = webdriver.Chrome('C:/Everything/chromedriver.exe')
    driver.get("https://www.redfin.com/")
    searchbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "searchInputBox")))
    searchbox.clear()
    searchbox.send_keys("Houston")
    searchbox.send_keys(Keys.RETURN)
    price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-rf-test-id='price-filter']//input[@name='maxPrice']")))
    price.clear()
    price.send_keys('60000')
    capacity = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-rf-test-id='expandable-option-2']//input[@name='minBeds']")))
    capacity.clear()
    capacity.send_keys('4')
    capacity.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Four')]")))
finally:
    while len(driver.window_handles) > 0: pass
driver.quit()

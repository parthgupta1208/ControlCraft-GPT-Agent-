
from selenium import webdriver

# Setting up the Chrome driver
driver = webdriver.Chrome('C:/Everything/chromedriver.exe')

# Opening wikipedia.org
driver.get('https://www.wikipedia.org/')

# Finding the search box and entering 'alexander' as the search term
search_box = driver.find_element_by_name('search')
search_box.send_keys('alexander')

# Clicking the search button
search_button = driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
search_button.click()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_web_driver = "/Users/workpay/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_web_driver)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

artilce_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')

all_can = driver.find_element(By.LINK_TEXT, 'anyone can edit')

all_can.click()

search = driver.find_element(By.NAME, 'search')
search.send_keys('Python')
search.send_keys(Keys.ENTER)

# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_web_driver = "/Users/workpay/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_web_driver)

driver.get('http://secure-retreat-92358.herokuapp.com/')

fname = driver.find_element(By.NAME, 'fName')
fname.send_keys('dan')
lname = driver.find_element(By.NAME, 'lName')
lname.send_keys('Mbuthia')
email = driver.find_element(By.NAME, 'email')
email.send_keys('test4@mbuthia.com')

submit = driver.find_element(By.XPATH, '/html/body/form/button')
submit.click()

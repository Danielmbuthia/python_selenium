from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_web_driver = "/Users/workpay/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_web_driver)

driver.get(url='https://www.python.org/')

events_time = driver.find_elements(By.CLASS_NAME, 'event-widget time')
events_name = driver.find_elements(By.CLASS_NAME, 'event-widget a')
events = {}
event = {}
i = 0
for time in events_time:
    for name in events_name:
        event['time'] = time.text
        event['program'] = name.text
    events[i] = event
    i += 1

print(events)

driver.quit()

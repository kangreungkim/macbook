from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome(r"/Users/kangreung.kim/PythonProject/DreamparkAddPoint/chromedriver")
url = 'https://www.dreamparkcc.or.kr/07membership/membership01.asp'
driver.get(url)
action = ActionChains(driver)

time.sleep(2)
driver.find_element_by_id('ms_id').click()

action.send_keys('crane123').perform()
action.key_down(Keys.TAB).perform()
action.send_keys('aksnfk2!').perform()
action.key_down(Keys.TAB).perform()
action.key_down(Keys.ENTER).perform()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="skip_gnb"]/nav/ul/li[2]/a').click()

while True: pass
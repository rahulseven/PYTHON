from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
browser = webdriver.Chrome(executable_path="./chromedriver")
browser.get('http://www.google.com')
browser.find_element_by_id("")
sleep(5)
browser.quit()

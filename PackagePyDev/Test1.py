from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
browser = webdriver.Firefox(executable_path="/media/rahul/DATA/EC_python/python-selenium-basic/drivers/geckodriver")
browser.get('http://www.google.com')
sleep(5)
browser.quit()
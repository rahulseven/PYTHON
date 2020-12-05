import pytest
from selenium.webdriver import Firefox
from selenium import webdriver



@pytest.fixtures(scope = 'session')
def driver(request):
    driver = Firefox()
    request.addfinalizer(driver.quit(self))
    return driver
    
def test_1(webdriver):
    webdriver.get("")
    assert 'GOOGLE' in webdriver.title
    
def test_2(webdriver):
    webdriver.get("pytest")
    assert 'pytest' in webdriver.title
        
    
        
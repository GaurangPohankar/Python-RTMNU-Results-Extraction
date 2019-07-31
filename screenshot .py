import urllib.request
import time
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.support.ui import Select


#make sure that geckodriver in place with this file
#firefox should be installed
driver = webdriver.Firefox(executable_path='./geckodriver')
driver.maximize_window()

driver.get('http://www.python.org/')
driver.save_screenshot('python_org.png')
driver.quit()

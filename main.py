import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import pandas as pd
import numpy as np


#Define functions
# Sleep function 
def sleep(x):
    time.sleep(x)

# Wait for a certain measure of time before throwing an exception
def wait(x):
    driver.implicitly_wait(x)

# Click Function
def click_bann_byID(ID):
    actions = ActionChains(driver)
    akzeptieren = driver.find_element(By.ID, ID)
    actions.click(akzeptieren).perform()
    wait(10)
    sleep(0.5)

# Find Elements Function
def find_elements_HPCO(H,P,C,O):
    if website_name == 'jobware':
        header = driver.find_elements(By.TAG_NAME, H)
    else:
        header = driver.find_elements(By.CLASS_NAME, H)
    publish = driver.find_elements(By.CLASS_NAME, P)
    company = driver.find_elements(By.CLASS_NAME, C)
    ort = driver.find_elements(By.CLASS_NAME, O) 

    list_header = [title.text for title in header]
    list_publish = [pub.text for pub in publish]
    list_company = [comp.text for comp in company]
    list_ort = [o.text for o in ort]
    return list_header, list_publish, list_company, list_ort

# Scroll Down Function
def scroll_down(x):
    n=0
    while n < x:
        n+=1
        actions.key_down(Keys.PAGE_DOWN).perform()
        sleep(1.5)
        actions.key_down(Keys.PAGE_DOWN).perform()
        sleep(1.5)
        actions.key_down(Keys.PAGE_DOWN).perform()
        sleep(1.5)
        actions.key_down(Keys.PAGE_UP).perform()
        sleep(0.10)
        actions.key_down(Keys.PAGE_DOWN).perform()
        wait(10)
        sleep(2.5)

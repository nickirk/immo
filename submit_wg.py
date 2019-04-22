# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
def submit_app(ref):
    #change the location of the driver on your machine
    driver=webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
    #tabs = driver.getWindowHandles()
    #driver.switchTo().window(tabs.get(1))
    driver.get('https://www.wg-gesucht.de/nachricht-senden.html?message_ad_id='+ref)
    driver.implicitly_wait(10)
    #login_button = driver.find_element_by_xpath('//button[text()="Login"]')
    login_button = driver.find_elements_by_class_name('btn-textbtn')[1]
    login_button.click()
    driver.implicitly_wait(3)
    email = driver.find_element_by_id('login_email_username')
    email.send_keys('your login email address')
    passwd = driver.find_element_by_id('login_password')
    passwd.send_keys('your password')
    login_button1 = driver.find_elements_by_id('login_submit')[0]
    login_button1.click()
    driver.implicitly_wait(5)
    se_button1 = driver.find_elements_by_id('sicherheit_bestaetigung')
    timestamp = driver.find_elements_by_id('time_stamp')
    if (len(se_button1) < 1 or len(timestamp) != 0):
	print("Already sent message to this offer...")
        driver.quit()
	return 0
    else:
	se_button1=se_button1[0]
	se_button1.click()
    text_area = driver.find_element_by_id('message_input')
    text_area.clear()
    #text_area.send_keys("\n Hello, test")
    text_area.send_keys(u"write your message to the landlord here")
    submit_button1 = driver.find_element_by_xpath("//button[@data-ng-click='submit()' or contains(.,'Nachricht senden')]")
    #driver.implicitly_wait(10)
    time.sleep(5) #may not be required
    submit_button1.click()
    time.sleep(3) #may not be required
    #driver.implicitly_wait(10)
    try:
        submit_button = driver.find_element_by_xpath("//button[@data-ng-click='submit()' or contains(.,'Nachricht senden')]")
    except NoSuchElementException:
	print("Cannot find submit button!")
        driver.quit()
    else:
        ActionChains(driver).move_to_element(submit_button).perform()
        time.sleep(3) #may not be required
        #submit_button.click()
        driver.quit()

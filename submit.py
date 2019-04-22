# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
def submit_app(ref):
    driver=webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
    driver.get('https://www.immobilienscout24.de'+ref+'#/basicContact/email')
    driver.implicitly_wait(10)
    el = driver.find_element_by_id('contactForm-salutation')
    for option in el.find_elements_by_tag_name('option'):
        if option.text == 'Herr':
            option.click() # select() in earlier versions of webdriver
            break
    last_name = driver.find_element_by_id('contactForm-lastName')
    last_name.send_keys("last name")
    first_name = driver.find_element_by_id('contactForm-firstName')
    first_name.send_keys("first name")
    email = driver.find_element_by_id('contactForm-emailAddress')
    email.send_keys("youremail@gmail.com")
    street = driver.find_element_by_id('contactForm-street')
    street.send_keys("your current living street")
    house = driver.find_element_by_id('contactForm-houseNumber')
    house.send_keys("room number")
    post = driver.find_element_by_id('contactForm-postcode')
    post.send_keys("postcode")
    city = driver.find_element_by_id('contactForm-city')
    city.send_keys("city")
    text_area = driver.find_element_by_id('contactForm-Message')
    text_area.clear()
    #text_area.send_keys("\n Hello, test")
    text_area.send_keys(u"Hallo,\n\n your message to the landlord. keep the 'u' before the message to make showing German in the message available. use \n as newline in your message.")
    submit_button1 = driver.find_element_by_xpath("//button[@data-ng-click='submit()' or contains(.,'Anfrage senden')]")
    #driver.implicitly_wait(10)
    time.sleep(5) #may not be required
    submit_button1.click()
    time.sleep(3) #may not be required
    #driver.implicitly_wait(10)
    try:
        submit_button = driver.find_element_by_xpath("//button[@data-ng-click='submit()' or contains(.,'Anfrage senden')]")
    except NoSuchElementException:
        driver.quit()
    else:
        ActionChains(driver).move_to_element(submit_button).perform()
        time.sleep(3) #may not be required
        submit_button.click()
        driver.quit()

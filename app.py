from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Firefox()

browser.maximize_window()

browser.get('http://www.facebook.com')
username = ""
password = ""



user = browser.find_element_by_id('email')
passw = browser.find_element_by_id('pass')
try:
    logbtn = browser.find_element_by_id('loginbutton')
except NoSuchElementException:
    logbtn = browser.find_element_by_id("u_0_d")

user.send_keys(username)
passw.send_keys(password)
time.sleep(3)

logbtn.click()
time.sleep(4)

browser.get("https://www.facebook.com/events/birthdays/")
time.sleep(5)
bdlist = browser.find_elements_by_css_selector("._1mf")  # class="_1mf _1mj

if len(bdlist) == 0 :
    print("couldnt fetch the class name properly, FB changed the class name")



for bd in bdlist:
    action = webdriver.ActionChains(browser)
    action.click(bd)
    action.send_keys("Happy Birthday, wish you an amazing year")
    action.send_keys(Keys.RETURN)
    action.perform()
    bd.location_once_scrolled_into_view

    time.sleep(5)
    

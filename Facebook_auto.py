from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Firefox()

browser.maximize_window()

browser.get('http://www.facebook.com')
email = ""  # enter your email here
pass_word = "" # enter your password here

def locate_elements():
    global user 
    user = browser.find_element_by_id('email')
    global passw 
    passw = browser.find_element_by_id('pass')
    global logbtn
    try:
        logbtn = browser.find_element_by_id('loginbutton')
    except NoSuchElementException:
        logbtn = browser.find_element_by_id("u_0_d")
       
def send_message():
    browser.get("https://www.facebook.com/events/birthdays/")
    time.sleep(5)
    global bdlist
    bdlist = browser.find_elements_by_css_selector("form")  # class="_1mf _1mj" or "form"
    global bd_list_name
    bd_list_name = browser.find_elements_by_css_selector("a h2")
    print(len(bdlist))
    print(len(bd_list_name))

    if len(bdlist) == 0 :
        print("couldnt fetch the class name properly") # try changing the class name as shown above if no birthdays in your list it will also return 0

    for bd in bdlist:
        i = 0
        action = webdriver.ActionChains(browser)
        action.click(bd)
        action.send_keys("Happy Birthday "+ bd_list_name[i].text.split()[0] + ", wish you an amazing year")
        action.send_keys(Keys.RETURN)
        action.perform()
        bd.location_once_scrolled_into_view
        time.sleep(3)
        i += 1

def login(username,password):
    user.send_keys(username)
    passw.send_keys(password)
    time.sleep(3)
    logbtn.click()
    time.sleep(4)

def check_login():
    if re.search(r"login_attempt",str(browser.current_url)):
        newpass = input("you entered a wrong password, please enter the correct one : \n")
        locate_elements()
        login(email,newpass)
        check_login()
    else:
        send_message()

if __name__=="__main__":
    locate_elements()
    login(email,pass_word)
    time.sleep(4)
    check_login()
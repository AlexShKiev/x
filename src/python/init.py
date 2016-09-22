from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

#getstarted
driver.set_window_size(1024,768)
#enter URL to casino lobby
driver.get('http://sta-all-kiv-gt4-setup01-tcl01.nix.cydmodule.com:8080/casinolobby/home2.xhtml')

password = driver.find_element_by_class_name("header-links header-links-last navigation__item__button login-window").click()
#password.click()

username = driver.find_element_by_name("login")
username.send_keys("manager")

#test the first page of registration form


password.send_keys(Keys.RETURN)

#next = driver.find_element_by_name("submit").click()
#driver.implicitly_wait(10)

#test the second page of registration form

account = driver.find_element_by_id("account[name]")
account.send_keys("Greentechnology")
find_element_by_css_selector("select#help_desk_size = option[value='500-999']").click()

#next = driver.find_element_by_css_selector("a.button.button-orange.next.next-two").click()
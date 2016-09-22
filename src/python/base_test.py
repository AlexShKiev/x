import os, sys, inspect
from src.python.mainconf import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginEnv:
  #using class login from maincof to setup browser
    st = login()
  #using function setUpClass from class login
    st.setUpClass()

    def log_to_env(self):
        self.driver = webdriver.Firefox()
        username = self.driver.find_element_by_css_selector("input[name=login]")
        passw = self.driver.find_element_by_name("password")
        username.send_keys("manager")
        passw.send_keys("manager")
        self.driver.find_element_by_css_selector("input[type=submit]").click()

    def log_to_game(self):
            player = self.driver.find_element_by_css_selector("input[name=username]")
            player.send_keys("new_u2")


    def findGame(self):
        games = ['wildwild', 'koiprincess']
        for x in games:
            game =self.driver.find_element_by_partial_link_text(x).click()
            self.driver.implicitly_wait(3000)
            self.driver.find_element_by_id('undefined').click()
            sound = self.driver.find_element_by_id('soundSettingsButton')
            sound.click()

    #closing down browser
    dw =login
    dw.tearDown()

if __name__ == "__main__":
    le = LoginEnv()
    le.log_to_env()

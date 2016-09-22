#import unittest
from selenium import webdriver


class LoginEnv:
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://sta-kiv-gt2-setup01-spp-01.nix.cydmodule.com:8080/admin/tester.jsp")

    def log_to_env(self):
        username = self.driver.find_element_by_css_selector("input[name=login]")
        passw = self.driver.find_element_by_name("password")

        username.send_keys("manager")
        passw.send_keys("manager")

        self.driver.find_element_by_css_selector("input[type=submit]").click()

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    le = LoginEnv()
    le.setUpClass()
    le.log_to_env()
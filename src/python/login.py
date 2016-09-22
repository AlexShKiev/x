from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginEnv:
    @classmethod
    def setUpClass(cls):
        games = ['wildwildwest_not', 'koi_not']
        for x in games:
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

    def log_to_game(self):
        player = self.driver.find_element_by_css_selector("input[name=username]")
        player.send_keys("new_u2")
        game = self.driver.find_element_by_partial_link_text(x).click()

    def findGame(self):
        game =self.driver.find_element_by_partial_link_text('wildwild').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('undefined').click()
        sound = self.driver.find_element_by_id('soundSettingsButton')
        sound.click()

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    le = LoginEnv()
    le.setUpClass()
    le.log_to_env()
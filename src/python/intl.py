from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


games = ['wildwildwest_not_mobile', 'koiprincess_not_mobile']

for x in games:
    driver = webdriver.Firefox()

#getstarted
    driver.maximize_window()
#enter URL to casino lobby
    driver.get('http://sta-kiv-gt2-setup01-spp-01.nix.cydmodule.com:8080/admin/tester.jsp')


    password = driver.find_element_by_name("password")
    password.send_keys("manager")

    username= driver.find_element_by_css_selector("input[name=login]")
    username.send_keys("manager")

    password.send_keys(Keys.RETURN)

    player = driver.find_element_by_css_selector("input[name=username]")
    player.send_keys("new_u2")

    player.send_keys(Keys.RETURN)

    game = driver.find_element_by_partial_link_text(x).click()

    #driver.implicitly_wait(24000)

    #3actions = ActionChains(driver)
    #actions.move_by_offset(683, 568)
    #actions.click()
    #actions.perform()

    try:
        element = WebDriverWait(driver, 9999).until(
            EC.presence_of_element_located((By.ID, "undefined"))
        )
    finally:
         driver.find_element_by_id('undefined').click()


    try:
        element = WebDriverWait(driver, 9999).until(
            EC.presence_of_element_located((By.ID, "soundSettingsButton"))
        )
    finally:
        driver.find_element_by_id('soundSettingsButton').click()

    #try: element = WebDriverWait(driver, 9999).until(
            #EC.presence_of_element_located((By.ID, "gameRules_rules"))
        #)
    #finally:
        #driver.find_element_by_id('gameRulesButton').click()


    driver.close()






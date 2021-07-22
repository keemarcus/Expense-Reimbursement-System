from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class LoginPage:
    email_box_id = 'email'
    password_box_id = 'password'
    login_button_id = 'login_button'
    logout_button_id = 'logout'

    def __init__(self, driver):
        self.driver = driver

    def enter_credentials(self):
        self.driver.find_element_by_id(self.email_box_id).send_keys('test@email.com')
        self.driver.find_element_by_id(self.password_box_id).send_keys('password')

    def enter_manager_credentials(self):
        self.driver.find_element_by_id(self.email_box_id).send_keys('testadmin@email.com')
        self.driver.find_element_by_id(self.password_box_id).send_keys('password')

    def click_submit_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def hit_enter_button(self):
        self.driver.find_element_by_id(self.password_box_id).send_keys(Keys.ENTER)

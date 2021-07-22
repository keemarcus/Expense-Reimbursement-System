from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class HomePage:
    # visible when logged out
    email_box_id = 'email'
    password_box_id = 'password'
    login_button_id = 'login_button'
    logout_button_id = 'logout'
    # visible when logged in
    amount_box_id = 'amount'
    reason_box_id = 'reason'
    edit_button_xpath = '/html/body/table/tbody/tr/td[6]/button'
    submit_button_id = 'submit_button'
    reason_text_xpath = '/html/body/table/tbody/tr/td[3]'

    def __init__(self, driver):
        self.driver = driver

    def enter_credentials(self):
        self.driver.find_element_by_id(self.email_box_id).send_keys('test@email.com')
        self.driver.find_element_by_id(self.password_box_id).send_keys('password')

    def enter_manager_credentials(self):
        self.driver.find_element_by_id(self.email_box_id).send_keys('testadmin@email.com')
        self.driver.find_element_by_id(self.password_box_id).send_keys('password')

    def click_login_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def hit_enter_button_login(self):
        self.driver.find_element_by_id(self.password_box_id).send_keys(Keys.ENTER)

    def hit_enter_button(self):
        self.driver.find_element_by_id(self.reason_box_id).send_keys(Keys.ENTER)

    def check_for_logout_button(self):
        try:
            self.driver.find_element_by_id(self.login_button_id)
        except NoSuchElementException:
            return False
        return True

    def enter_reimbursement_info(self):
        self.driver.find_element_by_id(self.reason_box_id).send_keys('automation testing')

    def click_submit_button(self):
        self.driver.find_element_by_id(self.submit_button_id).click()

    def hit_enter_button_reimbursement(self):
        self.driver.find_element_by_id(self.reason_box_id).send_keys(Keys.ENTER)

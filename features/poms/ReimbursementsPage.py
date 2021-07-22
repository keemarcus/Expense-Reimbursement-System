from selenium.webdriver.common.keys import Keys


class ReimbursementsPage:
    amount_box_id = 'amount'
    reason_box_id = 'reason'
    edit_button_xpath = '/html/body/table/tbody/tr[1]/td[6]/button'
    submit_button_id = 'submit_button'
    edit_submit_button_id = 'edit_submit_button'
    reason_text_xpath = '/html/body/table/tbody/tr[1]/td[3]'
    reimbursement_table_id = 'reimbursement table'
    reimbursements_xpath = '/html/body/table/tbody/tr'

    def __init__(self, driver):
        self.driver = driver

    def enter_reimbursement_info(self):
        self.driver.find_element_by_id(self.reason_box_id).send_keys('automation testing')

    def click_edit_button(self):
        self.driver.find_element_by_xpath(self.edit_button_xpath).click()

    def click_submit_button(self):
        self.driver.find_element_by_id(self.submit_button_id).click()

    def click_edit_submit_button(self):
        self.driver.find_element_by_id(self.edit_submit_button_id).click()

    def hit_enter_button(self):
        self.driver.find_element_by_id(self.reason_box_id).send_keys(Keys.ENTER)

    def check_for_created_reimbursement(self):
        self.driver.implicitly_wait(5)
        reason = self.driver.find_element_by_xpath(self.reason_text_xpath)
        return str(reason.text)

    def check_for_updated_reimbursement(self):
        self.driver.implicitly_wait(5)
        reason = self.driver.find_element_by_xpath(self.reason_text_xpath)
        return str(reason.text)

    def check_for_reimbursements(self):
        self.driver.implicitly_wait(5)
        table_size = len(self.driver.find_elements_by_xpath(self.reimbursements_xpath))
        return int(table_size)
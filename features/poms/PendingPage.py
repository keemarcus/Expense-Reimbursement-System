from selenium.webdriver.common.keys import Keys


class PendingPage:
    reimbursement_id = 0

    comment_box_xpath = '/html/body/table/tbody/tr[2]/td[5]/input'
    result_xpath = '/html/body/table/tbody/tr[2]/td[6]/select'
    deny_xpath = '/html/body/table/tbody/tr[2]/td[6]/select/option[3]'
    submit_xpath = '/html/body/table/tbody/tr[2]/td[7]/input'
    id_xpath = '/html/body/table/tbody/tr[2]/td[1]'
    reimbursements_xpath = '/html/body/table/tbody/tr'
    # edit_button_xpath = '/html/body/table/tbody/tr[1]/td[6]/button'
    # submit_button_id = 'submit_button'
    # edit_submit_button_id = 'edit_submit_button'
    # reason_text_xpath = '/html/body/table/tbody/tr[1]/td[3]'

    def __init__(self, driver):
        self.driver = driver

    def enter_review_info(self):
        self.driver.find_element_by_xpath(self.comment_box_xpath).send_keys('automation testing')
        self.driver.find_element_by_xpath(self.result_xpath).click()
        self.driver.find_element_by_xpath(self.deny_xpath).click()

    def get_reimbursement_id(self):
        self.reimbursement_id = self.driver.find_element_by_xpath(self.id_xpath).text
        return self.reimbursement_id

    def check_reimbursement_id(self):
        return self.driver.find_element_by_xpath(self.id_xpath).text != self.reimbursement_id

    def click_submit_button(self):
        self.driver.find_element_by_xpath(self.submit_xpath).click()

    def hit_enter_button(self):
        self.driver.find_element_by_xpath(self.comment_box_xpath).send_keys(Keys.ENTER)

    def check_for_reimbursements(self):
        self.driver.implicitly_wait(5)
        table_size = len(self.driver.find_elements_by_xpath(self.reimbursements_xpath))
        return int(table_size)
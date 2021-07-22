from selenium.webdriver.common.keys import Keys


class ReviewsPage:
    reviews_xpath = '/html/body/table/tbody/tr'
    edit_button_xpath = '/html/body/table/tbody/tr[1]/td[8]/button'
    submit_button_id = 'submit_button'
    comment_box_id = 'edit_comments'
    result_id = 'edit_result'
    deny_id = 'denied'
    comment_text_xpath = '/html/body/table/tbody/tr[1]/td[5]'

    def __init__(self, driver):
        self.driver = driver

    def enter_review_info(self):
        self.driver.find_element_by_id(self.comment_box_id).clear()
        self.driver.find_element_by_id(self.comment_box_id).send_keys('automation testing updated')
        self.driver.find_element_by_id(self.result_id).click()

    def click_edit_button(self):
        self.driver.find_element_by_xpath(self.edit_button_xpath).click()

    def click_submit_button(self):
        self.driver.find_element_by_id(self.submit_button_id).click()

    def get_reimbursement_id(self):
        pass

    def hit_enter_button(self):
        self.driver.find_element_by_id(self.comment_box_id).send_keys(Keys.ENTER)

    def check_for_updated_review(self):
        self.driver.implicitly_wait(5)
        reason = self.driver.find_element_by_xpath(self.comment_text_xpath)
        return str(reason.text)

    def check_for_reviews(self):
        self.driver.implicitly_wait(5)
        table_size = len(self.driver.find_elements_by_xpath(self.reviews_xpath))
        return int(table_size)
class PastReimbursementsPage:
    reimbursements_xpath = '/html/body/table/tbody/tr'

    def __init__(self, driver):
        self.driver = driver

    def check_for_reimbursements(self):
        self.driver.implicitly_wait(5)
        table_size = len(self.driver.find_elements_by_xpath(self.reimbursements_xpath))
        return int(table_size)
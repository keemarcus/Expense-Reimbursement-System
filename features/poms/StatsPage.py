class StatsPage:
    stats_xpath = '/html/body/table/tbody/tr'

    def __init__(self, driver):
        self.driver = driver

    def check_for_stats(self):
        self.driver.implicitly_wait(5)
        table_size = len(self.driver.find_elements_by_xpath(self.stats_xpath))
        return int(table_size)

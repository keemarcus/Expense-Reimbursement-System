from selenium import webdriver
from features.poms.LoginPage import LoginPage


def before_scenario(context, scenario):
    # we will start each test by opening a new browser window
    context.driver = webdriver.Chrome()


def after_scenario(context, scenario):
    # we will end each test by closing our browser window
    context.driver.quit()

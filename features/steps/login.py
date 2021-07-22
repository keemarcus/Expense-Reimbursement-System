from behave import *
from features.poms.LoginPage import LoginPage
from features.poms.HomePage import HomePage


@given('a user is on the home page')
def test_on_home_page(context):
    context.driver.get('http://localhost:5000')
    context.sll_page = HomePage(context.driver)


@given('a user is on the login page')
def test_on_login_page(context):
    context.driver.get('http://localhost:5000/login.html')
    context.sll_page = LoginPage(context.driver)


@given('a user enters the correct username and the correct password')
def test_user_enters_credentials(context):
    context.driver.implicitly_wait(1)
    context.sll_page.enter_credentials()


@when('the user pushes the submit button')
def test_user_clicks_submit(context):
    context.sll_page.click_submit_button()


@when('the user pushes the submit button to login')
def test_user_clicks_submit(context):
    context.sll_page.click_login_button()


@when('the user hits the enter button')
def test_user_hits_enter(context):
    context.driver.implicitly_wait(1)
    context.sll_page.hit_enter_button()


@when('the user hits the enter button to login')
def test_user_hits_enter(context):
    context.driver.implicitly_wait(1)
    context.sll_page.hit_enter_button_login()


@then('the user is logged in and redirected to the home page')
def test_user_redirected_after_using_enter(context):
    assert 'home' in context.driver.current_url
    context.sll_page = HomePage(context.driver)
    assert context.sll_page.check_for_logout_button() is True


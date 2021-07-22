from behave import *
from features.poms.LoginPage import LoginPage
from features.poms.HomePage import HomePage
from features.poms.ReimbursementsPage import ReimbursementsPage


@given('a user is logged in')
def log_in_as_user(context):
    context.driver.get('http://localhost:5000')
    context.sll_page = LoginPage(context.driver)
    context.driver.implicitly_wait(1)
    context.sll_page.enter_credentials()
    context.sll_page.hit_enter_button()
    assert 'home' in context.driver.current_url
    context.sll_page = HomePage(context.driver)
    assert context.sll_page.check_for_logout_button() is True


@given('a user is on their reimbursements page')
def test_on_reimbursements_page(context):
    context.driver.get('http://localhost:5000/reimbursements.html')
    context.sll_page = ReimbursementsPage(context.driver)


@when('the user enters a valid amount and reason')
def test_enter_reimbursement_info(context):
    context.sll_page.enter_reimbursement_info()


@when('the user pushes the edit submit button')
def test_user_clicks_submit(context):
    context.driver.implicitly_wait(1)
    context.sll_page.click_edit_submit_button()


@when('the user pushes the edit button')
def test_user_clicks_edit(context):
    context.driver.implicitly_wait(5)
    context.sll_page.click_edit_button()


@then('the user is redirected to their reimbursements page')
def test_on_reimbursements_page(context):
    assert 'reimbursements' in context.driver.current_url
    context.sll_page = ReimbursementsPage(context.driver)


@then('a new reimbursement request was created')
def test_reimbursement_created(context):
    assert context.sll_page.check_for_created_reimbursement() == 'automation testing'


@then('the reimbursement information is updated')
def test_reimbursement_updated(context):
    assert context.sll_page.check_for_updated_reimbursement() == 'automation testing'


@then('some reimbursements are displayed')
def test_reimbursements_displayed(context):
    assert context.sll_page.check_for_reimbursements() > 0


from behave import *
from features.poms.HomePage import HomePage
from features.poms.PendingPage import PendingPage
from features.poms.ReviewsPage import ReviewsPage
from features.poms.PastReimbursementsPage import PastReimbursementsPage
from features.poms.StatsPage import StatsPage


@given('a user is logged in as a manager')
def log_in_as_manager(context):
    context.driver.get('http://localhost:5000')
    context.sll_page = HomePage(context.driver)
    context.driver.implicitly_wait(1)
    context.sll_page.enter_manager_credentials()
    context.sll_page.hit_enter_button_login()
    assert 'home' in context.driver.current_url
    assert context.sll_page.check_for_logout_button() is True


@given('a manager is on the pending reviews page')
def test_on_pending_page(context):
    context.driver.get('http://localhost:5000/pending.html')
    context.sll_page = PendingPage(context.driver)


@given('a manager is on their reviews page')
def test_on_reviews_page(context):
    context.driver.get('http://localhost:5000/reviews.html')
    context.sll_page = ReviewsPage(context.driver)


@given('a manager is on the past reimbursements page')
def test_on_reviews_page(context):
    context.driver.get('http://localhost:5000/past_reimbursements.html')
    context.sll_page = PastReimbursementsPage(context.driver)


@given('a manager is on the statistics page')
def test_on_stats_page(context):
    context.driver.get('http://localhost:5000/stats.html')
    context.sll_page = StatsPage(context.driver)


@when('the manager enters a valid comment and result')
def test_enter_info(context):
    context.driver.implicitly_wait(5)
    context.sll_page.get_reimbursement_id()
    context.sll_page.enter_review_info()


@then('the reimbursement request is no longer pending')
def check_for_reimbursement(context):
    context.driver.implicitly_wait(5)
    assert context.sll_page.check_reimbursement_id()


@then('some review results are displayed')
def check_for_reviews(context):
    assert context.sll_page.check_for_reviews() > 0


@then('the reimbursement request is updated')
def check_for_update(context):
    assert context.sll_page.check_for_updated_review() == 'automation testing updated'


@then('all past reimbursements are displayed')
def check_for_past_reimbursement(context):
    context.driver.implicitly_wait(5)
    assert context.sll_page.check_for_reimbursements() > 0


@then('the statistics are displayed')
def check_for_stats(context):
    context.driver.implicitly_wait(5)
    assert context.sll_page.check_for_stats() > 0

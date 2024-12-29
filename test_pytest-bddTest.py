import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils

scenarios('features/orderTransactions.feature')


@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('order is placed for an item by user with {username} and {password}'))
def place_order_for_an_item(playwright, username, password, shared_data):
    user_credentials = {}
    user_credentials["userEmail"] = username
    user_credentials["userPassword"] = password

    api_utils = APIUtils()
    created_order_id = api_utils.createOrder(playwright, user_credentials)
    shared_data['order_id'] = created_order_id


@given('the user is on the landing page')
def user_is_on_landing_page(browserInstance, shared_data):
    login_page = LoginPage(browserInstance)  # creating object of LoginPage class
    login_page.nagigateTo()
    shared_data['login_page'] = login_page

@when(parsers.parse('user login to the portal with {username} and {password}'))
def user_login_to_the_portal(username, password, shared_data):
    loginpage = shared_data['login_page']
    dashboardpage = loginpage.login(username, password)
    shared_data['dashboard_page'] = dashboardpage

@when('navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboardpage = shared_data['dashboard_page']
    orderHistoryPage = dashboardpage.selectOrdersNavLink()
    shared_data['order_history_page'] = orderHistoryPage


@when('select the orderId')
def select_the_order(shared_data):
    orderHistoryPage = shared_data['order_history_page']
    created_order_id = shared_data['order_id']
    orderDetialsPage = orderHistoryPage.selectOrder(created_order_id)
    shared_data['order_details_page'] = orderDetialsPage


@then('order message is successfully displayed')
def validate_order_message_displayed_successfully(shared_data):
    orderDetialsPage = shared_data['order_details_page']
    message = orderDetialsPage.getMsgDisplayed()
    assert message == "Thank you for Shopping With Us"



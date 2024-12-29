import json

import pytest
from playwright.sync_api import Playwright

from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils

# Json file -> util(to convert json into python object) -> access into test
with open("data/credentials.json") as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']

#username: automationuser@gmail.com
#password: Superm@n001
#Url: https://rahulshettyacademy.com/client/
@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright:Playwright, browserInstance, user_credentials):

    # orders history page-> order is present
    api_utils = APIUtils()
    created_order_id = api_utils.createOrder(playwright, user_credentials)

    user_email = user_credentials["userEmail"]
    user_password = user_credentials["userPassword"]

    #login
    login_page = LoginPage(browserInstance) #creating object of LoginPage class
    login_page.nagigateTo()
    dashboard_page = login_page.login(user_email, user_password)
    orderHistoryPage = dashboard_page.selectOrdersNavLink()

    orderDetialsPage = orderHistoryPage.selectOrder(created_order_id)
    message = orderDetialsPage.getMsgDisplayed()
    assert message == "Thank you for Shopping With Us"




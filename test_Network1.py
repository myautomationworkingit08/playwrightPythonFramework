import pytest
from playwright.sync_api import Page


empty_order_response = {"data":[],"message":"No Orders"}

# -> api call from browser -> api call contact server and return back response to browser -> browser use response to generate HTML
def intercept_order_response(route):
    route.fulfill(
        json=empty_order_response
    )


@pytest.mark.smoke
def test_Network1(page:Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_order_response)
    page.get_by_placeholder("email@example.com").fill("automationuser@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Superm@n001")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    empty_order_list_message = page.locator(".mt-4").text_content()
    print(empty_order_list_message)
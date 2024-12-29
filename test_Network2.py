from playwright.sync_api import Page, Playwright, expect
from pytest_playwright.pytest_playwright import new_context

from utils.apiBase import APIUtils


def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=676ee25de2b5443b1f05ef9a")

def test_Network2(page:Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("automationuser@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Superm@n001")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)

def test_session_storage(playwright:Playwright):
    api_utils = APIUtils()
    tokenVal = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token','{tokenVal}')""")
    #------------------------------------------------------------------------#
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()

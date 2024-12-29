from playwright.sync_api import Playwright

from utils.apiBase import APIUtils


#username: automationuser@gmail.com
#password: Superm@n001
#Url: https://rahulshettyacademy.com/client/
def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    #login
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("automationuser@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Superm@n001")
    page.locator("#login").click()

    #orders history page-> order is present
    api_utils = APIUtils()
    created_order_id = api_utils.createOrder(playwright)

    page.get_by_role("button", name="ORDERS").click()
    page.locator("tr").filter(has_text=created_order_id).get_by_role("button",name="View").click()
    message_displayed = page.locator(".email-preheader p").text_content()
    assert message_displayed == "Thank you for Shopping With Us"



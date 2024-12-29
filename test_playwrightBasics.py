import time

from playwright.sync_api import Page, expect, Playwright


#we will use this approach to launch the browser when we need customizations
# like: running in headed mode, running in different browsers and etc.
def test_playwrightBasic(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

#we will use this approach to launch the browser when we don't need customizations
#It will only work for chromium engine which includes Chrome and Edge browsers only.
# And by default it will run in headless mode.
#If we want to run the tests in Headed mode then we need to pass an argument during runtime.
def test_playwrightShortCut(page:Page):
    page.goto("https://rahulshettyacademy.com")

def test_playwrightCoreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning1234")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("link", name="terms and conditions").click()
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_firefoxBrowserTest(playwright:Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    firefoxContext = firefoxBrowser.new_context()
    firefoxPage = firefoxContext.new_page()
    firefoxPage.goto("https://rahulshettyacademy.com/loginpagePractise/")
    firefoxPage.get_by_label("Username:").fill("rahulshettyacademy")
    firefoxPage.get_by_label("Password:").fill("learning1234")
    firefoxPage.get_by_role("combobox").select_option("teach")
    firefoxPage.get_by_role("link", name="terms and conditions").click()
    firefoxPage.locator("#terms").check()
    firefoxPage.get_by_role("button", name="Sign In").click()
    expect(firefoxPage.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(10)

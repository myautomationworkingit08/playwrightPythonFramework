from email.policy import default

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="browser selection"
    )
    parser.addoption(
        "--app_url",
        action="store",
        default="https://rahulshettyacademy.com/client/",
        help="URL of Application to test"
    )


@pytest.fixture
def browserInstance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    #app_url = request.config.getoption("app_url")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #page.goto(app_url)
    yield page
    context.close()
    browser.close()

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param


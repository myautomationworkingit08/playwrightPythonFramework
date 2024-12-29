from .dashboard import DashboardPage


class LoginPage:

    def __init__(self, page):
        self.page = page


    def nagigateTo(self):
        self.page.goto("https://rahulshettyacademy.com/client/")


    def login(self, userEmail, userPassword):
        self.page.get_by_placeholder("email@example.com").fill(userEmail)
        self.page.get_by_placeholder("enter your passsword").fill(userPassword)
        self.page.locator("#login").click()
        return DashboardPage(self.page)
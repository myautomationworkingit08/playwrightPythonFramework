from .orderDetails import OrderDetailsPage


class OrderHistoryPage:

    def __init__(self, page):
        self.page = page


    def selectOrder(self, orderId):
        self.page.locator("tr").filter(has_text=orderId).get_by_role("button", name="View").click()
        return OrderDetailsPage(self.page)
class OrderDetailsPage:


    def __init__(self, page):
        self.page = page


    def getMsgDisplayed(self):
        message_displayed = self.page.locator(".email-preheader p").text_content()
        return message_displayed
        assert message_displayed == "Thank you for Shopping With Us"
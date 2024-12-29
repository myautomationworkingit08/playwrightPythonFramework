from playwright.sync_api import Playwright

ordersPayload = {"orders":[{"country":"India","productOrderedId":"6581ca979fd99c85e8ee7faf"}]}

class APIUtils:

    def getToken(self, playwright:Playwright):
        user_email = "automationuser@gmail.com"
        user_password = "Superm@n001"
        login_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        login_response = login_request_context.post(url="/api/ecom/auth/login",
                                   headers={"content-type":"application/json"},
                                   data={"userEmail":user_email,"userPassword":user_password}
                                   )
        assert login_response.ok
        print(login_response.json())
        res_body = login_response.json()
        print(res_body["token"])
        return res_body["token"]

    def createOrder(self, playwright:Playwright):
        token = self.getToken(playwright)
        create_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        create_order_response = create_request_context.post(url="/api/ecom/order/create-order",
                                                            headers={"content-type":"application/json",
                                                                    "Authorization": token
                                                                    },
                                                            data=ordersPayload
                                                            )
        create_order_res_body = create_order_response.json()
        created_order_id = create_order_res_body["orders"][0]
        print(created_order_id)
        return created_order_id

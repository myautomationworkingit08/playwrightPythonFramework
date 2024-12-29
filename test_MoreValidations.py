import time

from playwright.sync_api import Page, expect


def test_UIChecks(page:Page):

    # hide/display and placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    # AlertHandle
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()

    # AlertHandle
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top")

    # FrameHandle
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator(".text h2")).to_contain_text("Happy Subscibers")

    # table data Reading
    # Check the price of the rice is 37
    # identify the Price column
    # identify the Rice row
    # extract the price of the rice
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    totalHeaders = page.locator("table.table-bordered th").count()
    for index in range(totalHeaders):
        if page.locator("table.table-bordered th").nth(index).filter(has_text="Price").count()>0:
            priceColValue = index
            print(f"Price column value is: {priceColValue}")
            break
    riceRow = page.locator("tbody tr").filter(has_text="Rice")
    actRicePrice = riceRow.locator("td").nth(priceColValue).text_content()
    print(f"Actual price of rice is: "+actRicePrice)
    assert actRicePrice == "37"





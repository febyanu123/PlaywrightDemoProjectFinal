from playwright.sync_api import Page,expect
from Constants.constant import login_url
class TestDebugging:
    def test_admin_login(self,page: Page):
        page.goto(login_url)
        page.get_by_placeholder("Username").fill("admin")
        page.get_by_placeholder("Password").screenshot(path="Screenshots/image3.png").fill("admin1")
        # page.screenshot(path="Screenshots/image1.png",full_page=True)
        page.locator("//button[text()='Sign In']").click()
        #page.screenshot(path="Screenshots/image2.png", full_page=True)
        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin")
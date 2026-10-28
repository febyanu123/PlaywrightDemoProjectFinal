from playwright.sync_api import Page, expect
from Constants.constant import login_url
from Pages import admin_dashboard
from Pages.admin_dashboard import AdminDashboard
from Utilities.ExcelRead import ExcelReadClass
from Pages.login_page import LoginPage
import pytest
class TestAdminLogin:
    @pytest.mark.timeout(3000)
    def test_admin_login(self,page:Page):
        page.goto(login_url)
        page.get_by_placeholder("Username").fill("admin")
        page.get_by_placeholder("Password").fill("admin")
        page.locator("//button[text()='Sign In']").click()
        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin")
    @pytest.mark.flaky(reruns=2)
    def test_admin_login_data_driven(self,page:Page):
          page.goto(login_url)
          obj=ExcelReadClass()
          username1=obj.read_excel_cell(2,1)
          password1=obj.read_excel_cell(2,2)
          login=LoginPage(page)
          login.enter_username(username1)
          login.enter_password(password1)
          login.click_signin()
          expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin")

    @pytest.mark.order(2)
    @pytest.mark.endtoend
    def test_admin_invalid_login(self,page:Page):
        page.goto(login_url)
        obj = ExcelReadClass()
        username1 = obj.read_excel_cell(3, 2)
        password1 = obj.read_excel_cell(4, 2)
        login = LoginPage(page)
        login.enter_username(username1)
        login.enter_password(password1)
        login.click_signin()
        login.show_alert()
    @pytest.mark.smoke
    def test_admin_logout(self,page:Page):
        page.goto(login_url)
        obj = ExcelReadClass()
        username1 = obj.read_excel_cell(2, 1)
        password1 = obj.read_excel_cell(2, 2)
        login = LoginPage(page)
        login.enter_username(username1)
        login.enter_password(password1)
        login.click_signin()
        admin=AdminDashboard(page)
        admin.click_admin_icon()
        admin.click_logout_icon()
        expect(page).to_have_url(login_url)
    @pytest.mark.order(1)
    def test_admin_logout_pom_chaining(self,page:Page):
        page.goto(login_url)
        obj = ExcelReadClass()
        username1 = obj.read_excel_cell(2, 1)
        password1 = obj.read_excel_cell(2, 2)
        login = LoginPage(page)
        login.enter_username(username1).enter_password(password1).click_signin().click_admin_icon().click_logout_icon()
        expect(page).to_have_url(login_url)





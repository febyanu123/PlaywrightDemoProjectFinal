import pytest
from playwright.sync_api import Page, expect
from Constants.constant import login_url
from Pages import admin_dashboard
from Pages.admin_dashboard import AdminDashboard
from Utilities.ExcelRead import ExcelReadClass
from Pages.login_page import LoginPage
class TestAdminDashboard:
    @pytest.mark.smoke
    @pytest.mark.sanity
    def test_admin_adduser(self,page:Page):
        page.goto(login_url)
        obj = ExcelReadClass()
        username1 = obj.read_excel_cell(2, 1)
        password1 = obj.read_excel_cell(2, 2)
        login = LoginPage(page)
        login.enter_username(username1)
        login.enter_password(password1)
        login.enter_username(username1).enter_password(password1).click_signin().click_more_info_link().click_new_button().enter_username_new("Festin").enter_password_new("123467").enter_usertype().enter_save_button().isPopupVisible_new_user()

    @pytest.mark.sanity
    def test_admin_search_user(self,page:Page):
        page.goto(login_url)
        obj = ExcelReadClass()
        username1 = obj.read_excel_cell(2, 1)
        password1 = obj.read_excel_cell(2, 2)
        login = LoginPage(page)
        login.enter_username(username1)
        login.enter_password(password1)
        login.enter_username(username1).enter_password(password1).click_signin().click_more_info_link().main_search_button().enter_search_username().enter_search_usertype().click_search_admin_users()


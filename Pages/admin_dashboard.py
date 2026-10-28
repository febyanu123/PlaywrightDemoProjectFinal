class AdminDashboard:
    def __init__(self,page):
        self.page = page
        self.admin_icon=page.locator("//a[@data-toggle='dropdown']")
        self.logout_icon=page.locator("a[class='dropdown-item']").nth(1)
        self.more_info_link=page.locator("//a[@class='small-box-footer']").nth(1)
    def click_admin_icon(self):
        self.admin_icon.click()
        return self
    def click_logout_icon(self):
        from Pages.login_page import LoginPage
        self.logout_icon.click()
        return LoginPage(self.page)#circular import happens when POMS are working in relation to each other

    def click_more_info_link(self):
        from Pages.home_page import HomePage
        self.more_info_link.click()
        return HomePage(self.page)

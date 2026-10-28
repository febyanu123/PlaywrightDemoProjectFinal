class LoginPage:
    def __init__(self,page):
        self.page=page
        self.username=page.get_by_placeholder("Username")
        self.password=page.get_by_placeholder("Password")
        self.signin=page.locator("//button[text()='Sign In']")
        self.invalid_alert=page.locator("//div[@class='alert alert-danger alert-dismissible']")
    def enter_username(self,user1):
        self.username.fill(user1)
        return self
    def enter_password(self,password1):
        self.password.fill(password1)
        return self
    def click_signin(self):
        from Pages.admin_dashboard import AdminDashboard
        self.signin.click()
        return AdminDashboard(self.page)
    def show_alert(self):
        print(self.invalid_alert.text_content())
        return self

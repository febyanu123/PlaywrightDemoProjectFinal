class HomePage:
    def __init__(self, page):
        self.page = page
        self.new_button=page.locator("//a[@class='btn btn-rounded btn-danger']")
        self.username=page.locator("#username")
        self.password=page.locator("#password")
        self.usertype=page.locator("#user_type")
        self.save_button=page.locator("//button[@name='Create']")
        self.search_admin=page.locator("//a[@class='btn btn-rounded btn-primary']")
        self.search_user=page.locator("#un").nth(2)
        self.search_usertype=page.locator("#ut").nth(1)
        self.search_button_after_entering_values=page.locator("//button[@class='btn btn-block-sm btn-danger']").nth(1)
        self.negative_alert=page.locator("//div[@class='alert alert-danger alert-dismissible']")
        self.popup_field = page.locator("//div[contains(@class,'alert-danger')]")
        self.popup_field_new = page.locator("//div[contains(@class,'alert-success')]")
    def click_new_button(self):
        self.new_button.click()
        return self
    def enter_username_new(self,user1):
        self.username.fill(user1)
        return self
    def enter_password_new(self,pwd1):
        self.password.fill(pwd1)
        return self
    def enter_usertype(self):
        self.usertype.select_option("Staff")
        return self
    def enter_save_button(self):
        self.save_button.click()
        return self

    def isPopupVisible(self):
        return self.popup_field.text_content()

        # this method is for user created successfulyy case [based on alert-success]
    def isPopupVisible_new_user(self):
            print(self.popup_field_new.text_content())
    def main_search_button(self):
        self.search_admin.click()
        return self
    def enter_search_username(self,search_user):
        self.search_user.fill(search_user)
        return self
    def enter_search_usertype(self):
        self.search_usertype.select_option("Staff")
        return self
    def click_search_admin_users(self):
        self.search_button_after_entering_values.click()
        return self

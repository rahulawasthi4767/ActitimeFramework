import pytest
from pages.loginpage import LoginPage
from pages.createuser import CreateUser


@pytest.mark.usefixtures("test_set_up")
class TestLogin:
    def test_login(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_user_name()
        lp.enter_password()
        lp.click_on_login_button()

    def test_createnew_user(self):
        driver = self.driver
        lp = CreateUser(driver)
        lp.click_newuser_btn()
        lp.enter_username()
        lp.enter_password()
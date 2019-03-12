import time


class CreateUser:
    def __init__(self, driver):
        self.driver = driver
        self.user_menu = "//div[@class='label' and contains(text(),'Users')]"
        self.user_btn = "//span[text()='Create New User']"
        self.username = "//input[@type='text' and @name='username']"
        self.password = "//input[@type='password' and @name='passwordText']"
        self.repassword = "//input[@type='password' and @name='passwordTextRetype']"
        self.firstname = "//input[@name='firstName']"
        self.lastname = "//input[@name='lastName']"
        self.email = "//input[@name='email']"
        self.submit = "//input[@type='submit']"

    def click_newuser_btn(self):
        self.driver.find_element_by_xpath(self.user_menu).click()
        self.driver.find_element_by_xpath(self.user_btn).click()
        time.sleep(3)

    def enter_username(self):
        self.driver.find_element_by_xpath(self.username).send_keys("ABC")

    def enter_password(self):
        self.driver.find_element_by_xpath(self.username).send_keys("abc")




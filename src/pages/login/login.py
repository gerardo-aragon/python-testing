from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    locators = {
        'username_field': ('ID', "userName"),
        'password_field': ('ID', "password"),
        'login_button': ('ID', "button"),
        'admin_import_button': ('ID', "admins-import")
    }

    def username_type(self, user):
        self.username_field.send_keys(user)

    def password_type(self, password):
        self.password_field.send_keys(password)

    def login_button_click(self):
        self.login_button.click()

    def login(self, user, password):
        self.username_type(user)
        self.password_type(password)
        self.login_button_click()








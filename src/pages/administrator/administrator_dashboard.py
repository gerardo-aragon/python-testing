from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
class AdministratorDashboard(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    locators = {
        'search_field': ('ID', "searchInput"),
        'import_admin_button': ('ID', "admins-import"),
        'create_admin_button': ('XPATH', "//span[text()=' Crear administrador ']"),
        'edit_admin_icon': ('ID', "delete-btn"),
    }

    def click_create_admin_button(self):
        self.create_admin_button.click()



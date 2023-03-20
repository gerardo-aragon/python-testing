from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AdministratorDashboard(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    locators = {
        'search_field': ('ID', "searchInput"),
        'import_admin_button': ('ID', "admins-import"),
        'create_admin_button': ('XPATH', "//span[text()=' Crear administrador ']"),
        'edit_admin_icon': ('ID', "edit-btn"),
        'delete_admin_icon': ('ID', "delete-btn"),
        'delete_button': ('ID', "deleteButton"),
        'confirm_message_toast': ('XPATH', "//div[contains(@class, 'toast-message')]"),
    }

    @staticmethod
    def fill_admin_field(locator, field):
        locator.send_keys(field)

    def click_create_admin_button(self):
        self.create_admin_button.click()

    def edit_admin_icon_click(self):
        self.edit_admin_icon.click()

    def search_admin(self, name):
        self.fill_admin_field(self.search_field, name)

    def delete_admin_icon_click(self):
        self.delete_admin_icon.click()

    def delete_admin_button_click(self):
        self.delete_button.click()

    def is_toast_present(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast-message')]")))

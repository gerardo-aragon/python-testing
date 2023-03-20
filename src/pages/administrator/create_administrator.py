from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.preconditions import *
import datetime
import time


class CreateAdministrator(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    locators = {
        'id_field' : ('XPATH', "//input[contains(@ng-reflect-name, 'adminId')]"),
        'name_field': ('XPATH', "//input[contains(@ng-reflect-name, 'firstName')]"),
        'last_name_field': ('XPATH', "//input[contains(@ng-reflect-name, 'lastName')]"),
        'birth_date_field': ('XPATH', "//input[contains(@ng-reflect-name, 'birthDate')]"),
        'email_address_field': ('XPATH', "//input[contains(@ng-reflect-name, 'email')]"),
        'phone_field': ('XPATH', "//input[contains(@ng-reflect-name, 'phone')]"),
        'username_field': ('XPATH', "//input[contains(@ng-reflect-name, 'userName')]"),
        'password_field': ('XPATH', "//input[contains(@ng-reflect-name, 'password')]"),
        'confirm_password_field': ('XPATH', "//input[contains(@ng-reflect-name, 'confirmationPassword')]"),
        'create_admin_button': ('ID', "submit-btn"),
        'cancel_admin_button': ('ID', "cancel-btn"),
        'confirm_message_toast': ('XPATH', "//div[contains(@class, 'toast-message')]"),
        'edit_admin_icon': ('ID', "edit-btn"),
        'delete_admin_icon': ('ID', "delete-btn"),
        'update_admin_button': ('XPATH', "//span[contains(text(),' Actualizar Administrador ')]"),
        'search_field': ('ID', "searchInput"),
        'delete_button': ('ID', "deleteButton")
    }

    @staticmethod
    def fill_admin_field(locator, field):
        locator.send_keys(field)

    def create_admin_button_click(self):
        self.create_admin_button.click()

    def create_user_admin(self, id_field, name, last_name, birth_date, phone, user_name, password):
        email_address = str("user_admin_" + create_random_fields() + "@gmail.com")

        self.fill_admin_field(self.id_field, id_field)
        self.fill_admin_field(self.name_field, name)
        self.fill_admin_field(self.last_name_field, last_name)
        self.fill_admin_field(self.birth_date_field, birth_date)
        self.fill_admin_field(self.email_address_field, email_address)
        self.fill_admin_field(self.phone_field, phone)
        self.fill_admin_field(self.username_field, user_name)
        self.fill_admin_field(self.password_field, password)
        self.fill_admin_field(self.confirm_password_field, password)
        self.create_admin_button_click()
        
    def edit_admin_icon_click(self):
        self.edit_admin_icon.click()
        
    def edit_admin_button_click(self):
        self.update_admin_button.click()

    def search_admin(self, name):
        self.fill_admin_field(self.search_field, name)

    def edit_user_admin(self, name, last_name, phone):

        self.fill_admin_field(self.name_field, name)
        self.fill_admin_field(self.last_name_field, last_name)
        self.fill_admin_field(self.phone_field, phone)
        self.edit_admin_button_click()
    
    def delete_admin_icon_click(self):
        self.delete_admin_icon.click()
        
    def delete_admin_button_click(self):
        self.delete_button.click()

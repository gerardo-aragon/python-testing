from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.preconditions import *
import datetime
import time


class EditAdministrator(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    locators = {
        'name_field': ('XPATH', "//input[contains(@ng-reflect-name, 'firstName')]"),
        'last_name_field': ('XPATH', "//input[contains(@ng-reflect-name, 'lastName')]"),
        'phone_field': ('XPATH', "//input[contains(@ng-reflect-name, 'phone')]"),
        'update_admin_button': ('XPATH', "//span[contains(text(),' Actualizar Administrador ')]"),
    }

    @staticmethod
    def fill_admin_field(locator, field):
        locator.send_keys(field)

    def edit_admin_button_click(self):
        self.update_admin_button.click()

    def edit_user_admin(self, name, last_name, phone):

        self.fill_admin_field(self.name_field, name)
        self.fill_admin_field(self.last_name_field, last_name)
        self.fill_admin_field(self.phone_field, phone)
        self.edit_admin_button_click()

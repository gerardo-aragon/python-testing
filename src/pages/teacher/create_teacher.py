from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.preconditions import *
import datetime
import time


class CreateTeacher(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    locators = {
        'id_field' : ('XPATH', "//input[contains(@ng-reflect-name, 'teacherId')]"),
        'name_field': ('XPATH', "//input[contains(@ng-reflect-name, 'firstName')]"),
        'last_name_field': ('XPATH', "//input[contains(@ng-reflect-name, 'lastName')]"),
        'birth_date_field': ('XPATH', "//input[contains(@ng-reflect-name, 'birthDate')]"),
        'email_address_field': ('XPATH', "//input[contains(@ng-reflect-name, 'email')]"),
        'phone_field': ('XPATH', "//input[contains(@ng-reflect-name, 'phone')]"),
        'username_field': ('XPATH', "//input[contains(@ng-reflect-name, 'userName')]"),
        'password_field': ('XPATH', "//input[contains(@ng-reflect-name, 'password')]"),
        'confirm_password_field': ('XPATH', "//input[contains(@ng-reflect-name, 'confirmationPassword')]"),
        'create_admin_button': ('ID', "submit-btn"),
    }

    @staticmethod
    def fill_teacher_field(locator, field):
        locator.send_keys(field)

    def create_teacher_button_click(self):
        self.create_admin_button.click()

    def create_user_teacher(self, id_field, name, last_name, birth_date, phone, user_name, password):
        email_address = str("user_teacher_" + create_random_fields() + "@gmail.com")

        self.fill_teacher_field(self.id_field, id_field)
        self.fill_teacher_field(self.name_field, name)
        self.fill_teacher_field(self.last_name_field, last_name)
        self.fill_teacher_field(self.birth_date_field, birth_date)
        self.fill_teacher_field(self.email_address_field, email_address)
        self.fill_teacher_field(self.phone_field, phone)
        self.fill_teacher_field(self.username_field, user_name)
        self.fill_teacher_field(self.password_field, password)
        self.fill_teacher_field(self.confirm_password_field, password)
        self.create_teacher_button_click()

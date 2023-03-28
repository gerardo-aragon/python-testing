from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.preconditions import *
import datetime
import time


class CreateStudent(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    locators = {
        'id_field' : ('XPATH', "//input[contains(@ng-reflect-name, 'studentId')]"),
        'name_field': ('XPATH', "//input[contains(@ng-reflect-name, 'firstName')]"),
        'last_name_field': ('XPATH', "//input[contains(@ng-reflect-name, 'lastName')]"),
        'birth_date_field': ('XPATH', "//input[contains(@ng-reflect-name, 'birthDate')]"),
        'tutor_field': ('XPATH', "//input[contains(@ng-reflect-name, 'tutor')]"),
        'phone_field': ('XPATH', "//input[contains(@ng-reflect-name, 'phone')]"),
        'address_field': ('XPATH', "//input[contains(@ng-reflect-name, 'address')]"),
        'section_dropdown': ('ID', "groupSelect"),
        'create_student_button': ('ID', "submit-btn"),
        'section': ('XPATH', "//span[contains(@class, 'mat-option-text')]"),
    }

    @staticmethod
    def fill_student_field(locator, field):
        locator.send_keys(field)

    def create_student_button_click(self):
        self.create_student_button.click()

    def dropdown_section_click(self):
        self.section_dropdown.click()

    def section_click(self):
        self.section.click()

    def create_user_student(self, id_field, name, last_name, birth_date, tutor, phone, address):

        self.fill_student_field(self.id_field, id_field)
        self.fill_student_field(self.name_field, name)
        self.fill_student_field(self.last_name_field, last_name)
        self.fill_student_field(self.birth_date_field, birth_date)
        self.fill_student_field(self.tutor_field, tutor)
        self.fill_student_field(self.phone_field, phone)
        self.fill_student_field(self.address_field, address)
        self.dropdown_section_click()
        self.section_click()
        self.create_student_button_click()
        
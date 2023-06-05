from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.preconditions import *
import datetime
import time


class CreateSection(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    locators = {
        'name_field': ('XPATH', "//input[contains(@ng-reflect-name, 'name')]"),
        'teacher_dropdown': ('XPATH', "//mat-select[contains(@role, 'combobox')]"),
        'teacher': ('XPATH', "//span[contains(@class, 'mat-option-text')]"),
        'create_section_button': ('ID', "update-group-btn"),
    }

    @staticmethod
    def fill_student_field(locator, field):
        locator.send_keys(field)

    def dropdown_teacher_click(self):
        self.teacher_dropdown.click()

    def teacher_click(self):
        self.teacher.click()

    def create_section_button_click(self):
        self.create_section_button.click()

    def create_section(self, section_name):

        self.fill_student_field(self.name_field, section_name)
        self.dropdown_teacher_click()
        self.teacher_click()
        self.create_section_button_click()

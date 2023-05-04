from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.preconditions import *
import datetime
import time


class EditSchedule(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    locators = {
        'section': ('XPATH', "(//span[contains(@class, 'mat-option-text')])[2]"),
        'name_field':  ('ID', "name"),
        'subject_combobox': ('xpath', "(//div[contains(@class, 'mat-form-field-infix')])[3]"),
        'edit_schedule_button': ('ID', "editButton"),
    }

    @staticmethod
    def fill_student_field(locator, field):
        locator.send_keys(field)
        
    def schedule_edit_button_click(self):
        self.edit_schedule_button.click()

    def dropdown_section_click(self):
        self.section_dropdown.click()

    def section_click(self):
        self.section.click()

    def subject_dropdown_click(self):
        self.subject_combobox.click()
        
    def edit_schedule(self, name):
        self.fill_student_field(self.name_field, name)
        self.subject_dropdown_click()
        time.sleep(2)
        self.section_click()
        self.schedule_edit_button_click()
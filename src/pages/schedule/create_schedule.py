from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.preconditions import *
import datetime
import time


class CreateSchedule(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    locators = {
        'section_dropdown': ('xpath', "(//div[contains(@class, 'mat-form-field-infix')])[1]"),
        'section': ('XPATH', "(//span[contains(@class, 'mat-option-text')])[2]"),
        'name_field':  ('ID', "name"),
        'subject_combobox': ('xpath', "(//div[contains(@class, 'mat-form-field-infix')])[3]"),
        'create_schedule_button': ('ID', "createButton"),
    }

    @staticmethod
    def fill_student_field(locator, field):
        locator.send_keys(field)
        
    def dropdown_section_click(self):
        self.section_dropdown.click()
        
    def section_click(self):
        self.section.click()
        
    def create_schedule_button_click(self):
        self.create_schedule_button.click()

    def subject_dropdown_click(self):
        self.subject_combobox.click()
        
    def crate_new_schedule(self, name):
        self.dropdown_section_click()
        self.section_click()
        self.fill_student_field(self.name_field, name)
        self.subject_dropdown_click()
        time.sleep(2)
        self.section_click()
        self.create_schedule_button_click()
        
    def section_click_dash(self):
        self.dropdown_section_click()
        self.section_click()
        
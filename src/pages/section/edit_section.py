from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.preconditions import *
import datetime
import time


class EditSection(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    locators = {
        'name_field': ('xpath', "(//input[contains(@class, 'mat-input-element')])[1]"),
        'edit_section_button': ('ID', "update-group-btn"),
    }

    @staticmethod
    def fill_section_field(locator, field):
        locator.send_keys(field)

    def section_edit_button_click(self):
        self.edit_section_button.click()

    def edit_section(self, name):
        self.fill_section_field(self.name_field, name)
        self.section_edit_button_click()

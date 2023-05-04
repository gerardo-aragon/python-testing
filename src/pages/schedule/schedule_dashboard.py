from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import time

class ScheduleDashboard(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    locators = {
        'section_dropdown': ('xpath', "(//div[contains(@class, 'mat-form-field-infix')])[1]"),
        'section': ('XPATH', "(//span[contains(@class, 'mat-option-text')])[2]"),
        'add_schedule_button': ('XPATH', "//span[text()=' Agregar Horario ']"),
        'edit_schedule_icon': ('ID', "edit-btn"),
        'delete_schedule_icon': ('ID', "delete-btn"),
        'delete_button': ('ID', "deleteButton"),
        'confirm_message_toast': ('XPATH', "//div[contains(@class, 'toast-message')]"),
    }

    def dropdown_section_click(self):
        self.section_dropdown.click()

    def add_schedule_button_click(self):
        self.add_schedule_button.click()

    def edit_schedule_icon_click(self):
        self.edit_schedule_icon.click()

    def delete_admin_icon_click(self):
        self.delete_schedule_icon.click()

    def section_click(self):
        self.section.click()
        
    def delete_teacher_button_click(self):
        self.delete_button.click()

    def is_toast_present(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast-message')]")))

    def section_click_dash(self):
        time.sleep(2)
        self.dropdown_section_click()
        self.section_click()
        time.sleep(2)
        
    def edit_icon_click(self):
        self.edit_schedule_icon_click()
        
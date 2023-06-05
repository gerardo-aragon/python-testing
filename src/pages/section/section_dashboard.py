import time

from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SectionDashboard(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    locators = {
        'create_section_button': ('XPATH', "//span[text()=' Sección Nueva ']"),
        'search_field': ('ID', "searchInput"),
        'edit_section_icon': ('ID', "edit-btn"),
        'delete_section_icon': ('ID', "delete-btn"),
        'delete_button': ('ID', "deleteButton"),
    }

    @staticmethod
    def fill_section_field(locator, field):
        locator.send_keys(field)

    def click_create_section_button(self):
        self.create_section_button.click()

    def is_toast_present(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast-message')]")))

    def edit_section_icon_click(self):
        self.edit_section_icon.click()
        time.sleep(2)

    def search_section(self, name):
        self.fill_section_field(self.search_field, name)
        time.sleep(2)

    def delete_section_icon_click(self):
        self.delete_section_icon.click()

    def delete_section_button_click(self):
        self.delete_button.click()

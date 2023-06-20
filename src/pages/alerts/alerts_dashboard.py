import time

from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AlertsDashboard(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    locators = {
        'search_field': ('ID', "searchInput"),
        'notes_btn': ('XPATH', "(//button[contains(@class, 'notes-btn')])[1]"),
        'action_icon': ('XPATH', "(//td[contains(@class, 'cdk-column-actions')]//mat-icon)[1]"),
        'new_note_input': ('XPATH', "//textarea"),
        'add_note_btn': ('XPATH', "//span[text()=' Agregar nota ']"),
        'note': ('XPATH', "//h3[contains(.,'Test')]")
    }

    @staticmethod
    def fill_alerts_field(locator, field):
        locator.send_keys(field)

    def search_alerts(self, name):
        self.fill_alerts_field(self.search_field, name)
        time.sleep(2)

    def notes_click(self):
        self.notes_btn.click()

    def actions_icon_click(self):
        self.action_icon.click()

    def add_note_click(self):
        self.add_note_btn.click()

    def is_toast_present(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast-message')]")))

    def is_register_present(self):
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Registro']")))

    def create_note(self):
        self.notes_click()
        self.fill_alerts_field(self.new_note_input, "Nota")
        self.add_note_click()

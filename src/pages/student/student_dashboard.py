from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class StudentDashboard(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    locators = {
        'create_student_button': ('XPATH', "//span[text()=' Nuevo estudiante ']"),
        'search_field': ('ID', "searchInput"),
        'edit_student_icon': ('ID', "edit-btn"),
        'delete_student_icon': ('ID', "delete-btn"),
        'delete_button': ('ID', "deleteButton"),
    }

    @staticmethod
    def fill_student_field(locator, field):
        locator.send_keys(field)

    def click_create_student_button(self):
        self.create_student_button.click()

    def is_toast_present(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast-message')]")))

    def edit_student_icon_click(self):
        self.edit_student_icon.click()

    def search_student(self, name):
        self.fill_student_field(self.search_field, name)

    def delete_student_icon_click(self):
        self.delete_student_icon.click()

    def delete_student_button_click(self):
        self.delete_button.click()
        
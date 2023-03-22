from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TeacherDashboard(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        
    locators = {
        'create_teacher_button': ('XPATH', "//span[text()=' Crear docente ']"),
        'search_field': ('ID', "searchInput"),
        'edit_teacher_icon': ('ID', "edit-btn"),
        'delete_teacher_icon': ('ID', "delete-btn"),
        'delete_button': ('ID', "deleteButton"),
    }

    @staticmethod
    def fill_teacher_field(locator, field):
        locator.send_keys(field)
        
    def click_create_teacher_button(self):
        self.create_teacher_button.click()
        
    def is_toast_present(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast-message')]")))
        
    def edit_teacher_icon_click(self):
        self.edit_teacher_icon.click()

    def search_teacher(self, name):
        self.fill_teacher_field(self.search_field, name)

    def delete_teacher_icon_click(self):
        self.delete_teacher_icon.click()

    def delete_teacher_button_click(self):
        self.delete_button.click()

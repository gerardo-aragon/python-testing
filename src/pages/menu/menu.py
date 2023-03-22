from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Menu(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    locators = {
        'administrator_link': ('XPATH', "//span[text()=' Administradores ']"),
        'teacher_link': ('XPATH', "//span[text()=' Docentes ']"),
        'alerts_link': ('XPATH', "//span[text()=' Alertas ']"),
        'students_link': ('XPATH', "//span[text()=' Estudiantes ']"),
        'schedule_link': ('XPATH', "//span[text()=' Horarios ']"),
        'subject_link': ('XPATH', "//span[text()=' Materias ']"),
        'section_link': ('XPATH', "//span[text()=' Secciones ']"),
        'logout_link': ('XPATH', "//span[text()=' Administradores ']"),
    }

    def click_administrator_link(self):
        self.administrator_link.click()

    def click_alerts_link(self):
        self.alerts_link.click()
        
    def click_teacher_link(self):
        self.teacher_link.click()

    def click_students_link(self):
        self.students_link.click()

    def click_schedule_link(self):
        self.schedule_link.click()

    def click_subject_link(self):
        self.subject_link.click()

    def click_suction_link(self):
        self.section_link.click()

    def click_logout_link(self):
        self.logout_link.click()

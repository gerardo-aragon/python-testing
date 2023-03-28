import time
from src.pages.login.login import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.student.create_student import CreateStudent
from src.pages.student.student_dashboard import StudentDashboard
from src.pages.student.edit_student import EditStudent
from src.pages.menu.menu import Menu
from utils.database_helper import *
from src.endpoints.auth.auth import *
from utils.preconditions import *
from src.endpoints.student.student import *
import pytest
import psycopg2


@pytest.mark.usefixtures('driver_init')
@pytest.mark.usefixtures("auth")
class TestCreateStudent:

    def test_01_create_student(self, auth):
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver)
        student_dashboard = StudentDashboard(self.driver)
        student_create = CreateStudent(self.driver)
        student_api = StudentApi
        menu = Menu(self.driver)

        # Login
        self.driver.get("http://localhost:4200/login")
        login_page.login("gerardo.aragon", "Test123@")

        # Flow to create a student
        menu.click_students_link()
        student_dashboard.click_create_student_button()
        user_id = create_random_fields()
        student_create.create_user_student(user_id, "Automated", "student testing", "09/11/1992", "Parent", "60606060",
                                           "Address")

        # Validations
        student_dashboard.is_toast_present()
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//td[contains(@class, 'cdk-column-student') and text() = 'Automated student testing']")))

        # Delete the student
        student_api.delete_student_user(auth, 200, user_id)

    def test_02_edit_student(self, auth):
        login_page = LoginPage(self.driver)
        student_dashboard = StudentDashboard(self.driver)
        menu = Menu(self.driver)
        student_api = StudentApi()
        student_edit = EditStudent(self.driver)

        # Create student by API
        cedula_id = create_random_fields()
        student_api.post_create_student(auth, 201, cedula_id)

        # Login
        self.driver.get("http://localhost:4200/login")
        login_page.login("gerardo.aragon", "Test123@")

        # Flow to edit the student
        menu.click_students_link()
        student_dashboard.search_student("Student Automated")
        time.sleep(2)
        student_dashboard.edit_student_icon_click()
        student_edit.edit_user_student(" edited", " edited", "60606060")

        # Validation
        student_dashboard.is_toast_present()

        # Delete the created student
        student_api.delete_student_user(auth, 200, cedula_id)

    def test_03_delete_student(self, auth):
        login_page = LoginPage(self.driver)
        student_dashboard = StudentDashboard(self.driver)
        menu = Menu(self.driver)
        student_api = StudentApi()

        # Create student by API
        cedula_id = create_random_fields()
        student_api.post_create_student(auth, 201, cedula_id)

        # Login
        self.driver.get("http://localhost:4200/login")
        login_page.login("gerardo.aragon", "Test123@")

        # Flow to delete the student
        menu.click_students_link()
        student_dashboard.search_student("Student Automated")
        time.sleep(2)
        student_dashboard.delete_student_icon_click()
        student_dashboard.delete_student_button_click()


    def test_04_search_student(self, auth):
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver)
        student_dashboard = StudentDashboard(self.driver)
        menu = Menu(self.driver)
        student_api = StudentApi()

        # Create student by API
        cedula_id = create_random_fields()
        student_api.post_create_student(auth, 201, cedula_id)

        # Login
        self.driver.get("http://localhost:4200/login")
        login_page.login("gerardo.aragon", "Test123@")

        # Flow to search the student
        menu.click_students_link()
        student_dashboard.search_student("Student Automated")
        time.sleep(2)

        # Validation
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//td[contains(@class, 'cdk-column-student') and text() = 'Student Automated Upre'])[1]")))

        # Delete the student
        student_api.delete_student_user(auth, 200, cedula_id)
        
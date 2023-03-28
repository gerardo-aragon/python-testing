import time
from src.pages.login.login import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.teacher.teacher_dashboard import TeacherDashboard
from src.pages.teacher.create_teacher import CreateTeacher
from src.pages.teacher.edit_teacher import EditTeacher
from src.pages.menu.menu import Menu
from utils.database_helper import *
from src.endpoints.auth.auth import *
from utils.preconditions import *
from src.endpoints.teacher.teacher import *
import pytest
import psycopg2

@pytest.mark.usefixtures('driver_init')
@pytest.mark.usefixtures("auth")
class TestCreateTeacher:

    def test_01_create_teacher(self, auth):
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver)
        teacher_dashboard = TeacherDashboard(self.driver)
        teacher_create = CreateTeacher(self.driver)
        menu = Menu(self.driver)
        teacher_api = TeacherApi()

        # Login
        self.driver.get("http://localhost:4200/login")
        login_page.login("gerardo.aragon", "Test123@")

        # Flow to create the teacher
        menu.click_teacher_link()
        teacher_dashboard.click_create_teacher_button()
        user_id = create_random_fields()
        user_name = str("user_admin_" + user_id)
        teacher_create.create_user_teacher(user_id, "Automated", "Teacher testing", "09/11/1992", "60606060",
                                       user_name, "Test123@")

        # Validations
        teacher_dashboard.is_toast_present()
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//td[contains(@class, 'cdk-column-firstName') and text() = 'Automated']")))

        # Delete the teacher
        teacher_api.delete_teacher_user(auth, 200, user_id)

    def test_02_edit_teacher(self, auth):
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver)
        teacher_dashboard = TeacherDashboard(self.driver)
        teacher_api = TeacherApi()
        teacher_edit = EditTeacher(self.driver)
        menu = Menu(self.driver)

        # Create teacher by API
        cedula_id, email, user_name = create_parametrize_data()
        teacher_api.post_create_teacher(auth, 201, cedula_id, "user_teacher_" + email, "user_teacher_" + user_name)

        # Login
        self.driver.get("http://localhost:4200/login")
        login_page.login("gerardo.aragon", "Test123@")

        # Flow to edit the teacher
        menu.click_teacher_link()
        teacher_dashboard.search_teacher("Teacher Automated")
        time.sleep(2)
        teacher_dashboard.edit_teacher_icon_click()
        teacher_edit.edit_user_admin(" edited", " edited", "60606060")

        # Validation
        teacher_dashboard.is_toast_present()

        # Delete the created teacher
        teacher_api.delete_teacher_user(auth, 200, cedula_id)
    

    def test_03_delete_teacher(self, auth):
        teacher_api = TeacherApi()
        teacher_dashboard = TeacherDashboard(self.driver)
        login_page = LoginPage(self.driver)
        menu = Menu(self.driver)
        wait = WebDriverWait(self.driver, 10)

        # Create teacher by API
        cedula_id, email, user_name = create_parametrize_data()
        teacher_api.post_create_teacher(auth, 201, cedula_id, "user_teacher_" + email, "user_teacher_" + user_name)

        # Login
        self.driver.get("http://localhost:4200/login")
        login_page.login("gerardo.aragon", "Test123@")

        # Flow to delete the teacher
        menu.click_teacher_link()
        teacher_dashboard.search_teacher("Teacher Automated")
        teacher_dashboard.delete_teacher_icon_click()
        teacher_dashboard.delete_teacher_button_click()

        # Validation
        teacher_dashboard.is_toast_present()


    def test_04_search_teacher(self, auth):
        teacher_api = TeacherApi()
        teacher_dashboard = TeacherDashboard(self.driver)
        login_page = LoginPage(self.driver)
        menu = Menu(self.driver)
        wait = WebDriverWait(self.driver, 10)

        # Create teacher by API
        cedula_id, email, user_name = create_parametrize_data()
        teacher_api.post_create_teacher(auth, 201, cedula_id, "user_teacher_" + email, "user_teacher_" + user_name)

        # Login
        self.driver.get("http://localhost:4200/login")
        login_page.login("gerardo.aragon", "Test123@")

        # Flow to search the teacher
        menu.click_teacher_link()
        teacher_dashboard.search_teacher("Teacher Automated")

        # Validation
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//td[contains(@class, 'cdk-column-firstName') and text() = 'Teacher Automated'])[1]")))

        # Delete the teacher
        teacher_api.delete_teacher_user(auth, 200, cedula_id)

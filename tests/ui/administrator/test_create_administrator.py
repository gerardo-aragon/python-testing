import time
from src.pages.login.login import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.administrator.administrator_dashboard import AdministratorDashboard
from src.pages.administrator.create_administrator import CreateAdministrator
from src.pages.administrator.edit_administrator import EditAdministrator
from src.endpoints.administrator.administrator import *
from utils.database_helper import *
from src.endpoints.auth.auth import *
from utils.preconditions import *
import pytest
import psycopg2

@pytest.mark.usefixtures('driver_init')
@pytest.mark.usefixtures("auth")
class TestAdministrator:

    def test_01_create_administrator(self, auth):
        login_page = LoginPage(self.driver)
        api_admin = AdministratorApi()
        dashboard_admin = AdministratorDashboard(self.driver)
        create_admin = CreateAdministrator(self.driver)
        wait = WebDriverWait(self.driver, 10)

        # Login
        self.driver.get("http://localhost:4200/login")
        login_page.login("gerardo.aragon", "Test123@")

        # flow to create an admin
        dashboard_admin.click_create_admin_button()
        user_id = create_random_fields()
        user_name = str("user_admin_" + user_id)
        create_admin.create_user_admin(user_id, "Gerardo", "Aragón Madrigal", "09/11/1992", "60606060",
                                               user_name, "Test123@")

        # Validations
        dashboard_admin.is_toast_present()
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//td[contains(@class, 'mat-column-userName') and text() = '" + user_name + "']")))

        # Delete the created admin
        api_admin.delete_admin_user(auth, 200, user_id)


    def test_02_edit_admin(self, auth):
        login_page = LoginPage(self.driver)
        api_admin = AdministratorApi()
        dashboard_admin = AdministratorDashboard(self.driver)
        edit_admin = EditAdministrator(self.driver)
        wait = WebDriverWait(self.driver, 10)
        
        # Create admin by API
        cedula_id, email, user_name = create_parametrize_data()
        api_admin.post_create_administrator(auth, 201, cedula_id, "user_admin_" + email,
                                                        "user_admin_" + user_name)

        # Login
        self.driver.get("http://localhost:4200/login")
        login_page.login("gerardo.aragon", "Test123@")

        # Flow to edit the admin
        dashboard_admin.search_admin("Admin")
        time.sleep(2)
        dashboard_admin.edit_admin_icon_click()
        edit_admin.edit_user_admin(" edited", " edited", "60606060")

        # Validations
        dashboard_admin.is_toast_present()
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//td[contains(@class, 'mat-column-userName') and text() = 'user_admin_" + user_name + "']")))

        # Delete the created admin
        api_admin.delete_admin_user(auth, 200, cedula_id)
        
        
    def test_03_delete_admin(self, auth):
        login_page = LoginPage(self.driver)
        dashboard_admin = AdministratorDashboard(self.driver)
        api_admin = AdministratorApi()

        # Create admin by API
        cedula_id, email, user_name = create_parametrize_data()
        api_admin.post_create_administrator(auth, 201, cedula_id, "user_admin_" + email,
                                        "user_admin_" + user_name)

        # Login
        self.driver.get("http://localhost:4200/login")
        login_page.login("gerardo.aragon", "Test123@")

        # Flow to delete the admin
        dashboard_admin.search_admin("Admin")
        time.sleep(2)
        dashboard_admin.delete_admin_icon_click()
        dashboard_admin.delete_admin_button_click()

        # Validation
        dashboard_admin.is_toast_present()


    def test_04_search_admin(self, auth):
        login_page = LoginPage(self.driver)
        dashboard_admin = AdministratorDashboard(self.driver)
        api_admin = AdministratorApi()
        wait = WebDriverWait(self.driver, 10)

        # Create admin by API
        cedula_id, email, user_name = create_parametrize_data()
        api_admin.post_create_administrator(auth, 201, cedula_id, "user_admin_" + email,
                                        "user_admin_" + user_name)

        # Login
        self.driver.get("http://localhost:4200/login")
        login_page.login("gerardo.aragon", "Test123@")

        # Search the admin
        dashboard_admin.search_admin("Admin")
        time.sleep(2)

        # Validation
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//td[contains(@class, 'mat-column-userName') and text() = 'user_admin_" + user_name + "']")))

        # Delete the created admin
        api_admin.delete_admin_user(auth, 200, cedula_id)

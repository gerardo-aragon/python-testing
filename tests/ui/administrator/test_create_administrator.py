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
class TestCreateAdministrator:

    def test_01_create_administrator(self, auth):
        self.driver.get("http://localhost:4200/login")

        admin = AdministratorApi()

        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver)
        login_page.login("gerardo.aragon", "Test123@")

        admin_dashboard = AdministratorDashboard(self.driver)
        admin_dashboard.click_create_admin_button()

        create_admin = CreateAdministrator(self.driver)

        user_id = create_random_fields()
        user_name = str("user_admin_" + user_id)

        create_admin.create_user_admin(user_id, "Gerardo", "Aragón Madrigal", "09/11/1992", "60606060",
                                               user_name, "Test123@")
        admin_dashboard.is_toast_present()
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//td[contains(@class, 'mat-column-userName') and text() = '" + user_name + "']")))
        
        admin.delete_admin_user(auth, 200, user_id)


    def test_02_edit_admin(self, auth):
        admin = AdministratorApi()
        dashboard_admin = AdministratorDashboard(self.driver)
        edit_admin = EditAdministrator(self.driver)
        
        # Create admin
        cedula_id, email, user_name = create_parametrize_data()
        admin.post_create_administrator(auth, 201, cedula_id, "user_admin_" + email,
                                                        "user_admin_" + user_name)
        
        self.driver.get("http://localhost:4200/login")
        
        login_page = LoginPage(self.driver)
        login_page.login("gerardo.aragon", "Test123@")
        
        dashboard_admin.search_admin("Admin")
        dashboard_admin.edit_admin_icon_click()
        edit_admin.edit_user_admin(" edited", " edited", "60606060")

        dashboard_admin.is_toast_present()

        admin.delete_admin_user(auth, 200, cedula_id)
        
        
    def test_03_delete_admin(self, auth):
        admin = AdministratorApi()
        dashboard_admin = AdministratorDashboard(self.driver)

        # Create admin
        cedula_id, email, user_name = create_parametrize_data()
        admin.post_create_administrator(auth, 201, cedula_id, "user_admin_" + email,
                                        "user_admin_" + user_name)

        self.driver.get("http://localhost:4200/login")

        login_page = LoginPage(self.driver)
        login_page.login("gerardo.aragon", "Test123@")

        dashboard_admin.search_admin("Admin")
        dashboard_admin.delete_admin_icon_click()
        dashboard_admin.delete_admin_button_click()

        dashboard_admin.is_toast_present()


    def test_04_search_admin(self, auth):
        admin = AdministratorApi()
        dashboard_admin = AdministratorDashboard(self.driver)
        wait = WebDriverWait(self.driver, 10)

        # Create admin
        cedula_id, email, user_name = create_parametrize_data()
        admin.post_create_administrator(auth, 201, cedula_id, "user_admin_" + email,
                                        "user_admin_" + user_name)

        self.driver.get("http://localhost:4200/login")

        login_page = LoginPage(self.driver)
        login_page.login("gerardo.aragon", "Test123@")

        dashboard_admin.search_admin("Admin")

        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//td[contains(@class, 'mat-column-userName') and text() = 'user_admin_" + user_name + "']")))

        admin.delete_admin_user(auth, 200, cedula_id)

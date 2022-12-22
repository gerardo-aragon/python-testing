import time
from src.pages.login.login import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.administrator.administrator_dashboard import AdministratorDashboard
from src.pages.administrator.create_administrator import CreateAdministrator
from utils.database_helper import *
import pytest
import psycopg2

@pytest.mark.usefixtures('driver_init')
class TestCreateAdministrator:

    def test_01_create_administrator(self):
        self.driver.get("http://localhost:4200/login")

        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver)
        login_page.login("gerardo.aragon", "Test123@")

        admin_dashboard = AdministratorDashboard(self.driver)
        admin_dashboard.click_create_admin_button()

        create_admin = CreateAdministrator(self.driver)

        user_name = str("user_admin_" + create_admin.create_random_field())

        create_admin.create_user_admin("Gerardo", "Aragón Madrigal", "09/11/1992", "60606060",
                                               user_name, "Test123@")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast-message')]")))
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//td[contains(@class, 'mat-column-userName') and text() = '" + user_name + "']")))



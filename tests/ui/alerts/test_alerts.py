from src.pages.login.login import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.alerts.alerts_dashboard import *
from selenium.webdriver.common.by import By
from src.pages.menu.menu import Menu
from utils.database_helper import *
from src.endpoints.auth.auth import *
from utils.preconditions import *
from src.endpoints.faults.faults import *
import pytest
import psycopg2
import datetime
import time


@pytest.mark.usefixtures('driver_init')
@pytest.mark.usefixtures("auth")
class TestCreateNotes:

    def test_01_create_note(self, auth):
        self.driver.get("http://localhost:4200/login")

        login_page = LoginPage(self.driver)
        menu = Menu(self.driver)
        alerts_dashboard = AlertsDashboard(self.driver)

        create_fault(auth)

        # Login
        login_page.login("gerardo.aragon", "Test123@")

        # Access alerts section
        menu.click_alerts_link()

        # Create note
        alerts_dashboard.create_note()

        # Validate creation note
        alerts_dashboard.is_toast_present()

    def test_02_access_action_module(self, auth):
        self.driver.get("http://localhost:4200/login")

        login_page = LoginPage(self.driver)
        menu = Menu(self.driver)
        alerts_dashboard = AlertsDashboard(self.driver)

        create_fault(auth)

        # Login
        login_page.login("gerardo.aragon", "Test123@")

        # Access alerts section
        menu.click_alerts_link()

        # Access actions section
        alerts_dashboard.actions_icon_click()
        alerts_dashboard.is_register_present()

    def test_03_search_alert(self, auth):
        self.driver.get("http://localhost:4200/login")

        login_page = LoginPage(self.driver)
        menu = Menu(self.driver)
        alerts_dashboard = AlertsDashboard(self.driver)
        faults = FaultsApi()
        wait = WebDriverWait(self.driver, 10)

        create_fault(auth)
        faults_data = faults.get_student_faults(auth, 200)
        first_name = faults_data['data'][0]['firstName']
        last_name = faults_data['data'][0]['lastName']
        full_name = first_name + ' ' + last_name

        # Login
        login_page.login("gerardo.aragon", "Test123@")

        # Access alerts section
        menu.click_alerts_link()

        # Search alert
        alerts_dashboard.search_alerts(full_name)

        # Validate if the alert is present
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//td[contains(@class, 'cdk-column-students') and text() = '" + full_name + "']")))

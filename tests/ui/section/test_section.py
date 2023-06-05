import time
from src.pages.login.login import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.section.section_dashboard import SectionDashboard
from src.pages.section.edit_section import EditSection
from src.pages.section.create_section import *
from src.pages.menu.menu import Menu
from utils.database_helper import *
from src.endpoints.auth.auth import *
from utils.preconditions import *
import pytest
import psycopg2


@pytest.mark.usefixtures('driver_init')
@pytest.mark.usefixtures("auth")
class TestCreateStudent:

    def test_01_create_section(self):
        self.driver.get("http://localhost:4200/login")

        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver)
        section_dashboard = SectionDashboard(self.driver)
        section_create = CreateSection(self.driver)
        menu = Menu(self.driver)

        # Login
        login_page.login("gerardo.aragon", "Test123@")
        
        # Access section module
        menu.click_section_link()
        section_dashboard.click_create_section_button()

        # Create section
        random_name = create_random_fields()
        section_name = str("Section_" + random_name)
        section_create.create_section(section_name)

        #Validate if section was created
        section_dashboard.is_toast_present()
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//td[contains(@class, 'cdk-column-name') and text() = '" + section_name + "']")))
        
        
    def test_02_edit_section(self, auth):
        self.driver.get("http://localhost:4200/login")

        login_page = LoginPage(self.driver)
        group_api = GroupsApi()
        section_dashboard = SectionDashboard(self.driver)
        edit_section = EditSection(self.driver)
        menu = Menu(self.driver)

        # Create section
        group_name = "Sección " + (create_random_fields()[-5:])
        response_data = group_api.post_create_groups(auth, 201, group_name)
        section_id = response_data['created'][0]['id']

        # Login
        login_page.login("gerardo.aragon", "Test123@")

        # Access section module
        menu.click_section_link()

        # Edit section
        section_dashboard.search_section(group_name)
        section_dashboard.edit_section_icon_click()
        edit_section.edit_section("_edited")

        # Validate if toast is present
        section_dashboard.is_toast_present()

        # Delete the section to avoid unnecessary data
        group_api.delete_group(auth, 200, section_id)

    def test_03_delete_section(self, auth):
        self.driver.get("http://localhost:4200/login")

        login_page = LoginPage(self.driver)
        group_api = GroupsApi()
        section_dashboard = SectionDashboard(self.driver)
        menu = Menu(self.driver)

        # Create section
        group_name = "Sección " + (create_random_fields()[-5:])
        group_api.post_create_groups(auth, 201, group_name)

        # Login
        login_page.login("gerardo.aragon", "Test123@")

        # Access section module
        menu.click_section_link()

        # Delete section
        section_dashboard.search_section(group_name)
        section_dashboard.delete_section_icon_click()
        section_dashboard.delete_section_button_click()

        # Validate if toast is present
        section_dashboard.is_toast_present()


    def test_04_search_section(self, auth):
        self.driver.get("http://localhost:4200/login")

        login_page = LoginPage(self.driver)
        group_api = GroupsApi()
        section_dashboard = SectionDashboard(self.driver)
        wait = WebDriverWait(self.driver, 10)
        menu = Menu(self.driver)

        # Create section
        group_name = "Sección " + (create_random_fields()[-5:])
        response_data = group_api.post_create_groups(auth, 201, group_name)
        section_id = response_data['created'][0]['id']

        # Login
        login_page.login("gerardo.aragon", "Test123@")

        # Access section module
        menu.click_section_link()

        # Search section
        section_dashboard.search_section(group_name)
        time.sleep(2)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//td[contains(@class, 'cdk-column-name') and text() = '" + group_name + "'])")))

        # Delete the section to avoid unnecessary data
        group_api.delete_group(auth, 200, section_id)

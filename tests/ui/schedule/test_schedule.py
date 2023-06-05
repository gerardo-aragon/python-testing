from src.pages.login.login import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.menu.menu import Menu
from src.pages.schedule.schedule_dashboard import *
from src.pages.schedule.edit_schedule import *
from src.pages.schedule.create_schedule import *
from src.endpoints.schedule.schedule import *
from src.endpoints.groups.groups import *
from utils.database_helper import *
from src.endpoints.auth.auth import *
from utils.preconditions import *
import pytest
import psycopg2
import datetime
import time


@pytest.mark.usefixtures('driver_init')
@pytest.mark.usefixtures("auth")
class TestCreateSchedule:

    def test_01_create_schedule(self):
        self.driver.get("http://localhost:4200/login")

        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver)
        schedule_dashboard = ScheduleDashboard(self.driver)
        create_schedule = CreateSchedule(self.driver)
        menu = Menu(self.driver)

        # Login
        login_page.login("gerardo.aragon", "Test123@")

        # Access schedule section
        menu.click_schedule_link()

        # Create schedule
        schedule_dashboard.add_schedule_button_click()
        random_name = create_random_fields()
        schedule_name = str("Horario_" + random_name)
        create_schedule.crate_new_schedule(schedule_name)
        create_schedule.section_click_dash()

        # validate
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//td[contains(@class, 'mat-column-scheduleName') and text() = '" + schedule_name + "']")))

    def test_02_edit_schedule(self, auth):
        self.driver.get("http://localhost:4200/login")

        login_page = LoginPage(self.driver)
        schedule_dashboard = ScheduleDashboard(self.driver)
        edit_schedule = EditSchedule(self.driver)
        menu = Menu(self.driver)
        schedule_api = ScheduleApi()
        group_api = GroupsApi()

        # Search an existent group (Created previously by database)
        search_group = group_api.get_search_group(auth, 200, "7-1 (No eliminar)")
        group_id = search_group["data"][0]["id"]

        # Create schedule
        schedule_name = "Horario_" + (create_random_fields()[-5:])
        dictionary = schedule_api.post_create_schedule(auth, 201, schedule_name, group_id)
        schedule_id = dictionary["id"]

        #Login
        login_page.login("gerardo.aragon", "Test123@")

        # Access schedule section
        menu.click_schedule_link()

        # Edit schedule
        schedule_dashboard.section_click_dash()
        schedule_dashboard.edit_icon_click()
        edit_schedule.edit_schedule("_edited")

        # Validate if toast is present
        schedule_dashboard.is_toast_present()

        # Delete the schedule to avoid unnecessary data
        schedule_api.delete_schedule(auth, 200, schedule_id)

    def test_03_delete_schedule(self, auth):
        self.driver.get("http://localhost:4200/login")

        login_page = LoginPage(self.driver)
        schedule_dashboard = ScheduleDashboard(self.driver)
        menu = Menu(self.driver)
        schedule_api = ScheduleApi()
        group_api = GroupsApi()

        # Search an existent group (Created previously by database)
        search_group = group_api.get_search_group(auth, 200, "7-1 (No eliminar)")
        group_id = search_group["data"][0]["id"]

        # Create schedule
        schedule_name = "Horario_" + (create_random_fields()[-5:])
        dictionary = schedule_api.post_create_schedule(auth, 201, schedule_name, group_id)

        #Login
        login_page.login("gerardo.aragon", "Test123@")

        # Access schedule section
        menu.click_schedule_link()

        # Delete schedule
        schedule_dashboard.section_click_dash()
        schedule_dashboard.delete_admin_icon_click()
        schedule_dashboard.delete_teacher_button_click()

        # Validate if toast is present
        schedule_dashboard.is_toast_present()

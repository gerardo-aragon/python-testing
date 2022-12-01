import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.pages.login import LoginPage
from utils.database_helper import insert


@pytest.mark.usefixtures("driver_init")
class TestLogin:

    def test_login_admin(self):
        self.driver.get("https://upre-fe-dev.vercel.app/")

        wait = WebDriverWait(self.driver, 30)
        login_page = LoginPage(self.driver)
        login_page.login("admin@admin.com", "tempPass_admin@admin.com")
        wait.until(EC.visibility_of_element_located((By.ID, "admins-import")))

    def test_invalid_login(self):
        self.driver.get("https://upre-fe-dev.vercel.app/")

        wait = WebDriverWait(self.driver, 30)
        login_page = LoginPage(self.driver)
        login_page.login("admin@admin.com", "tempPass_admin@admi.com")
        wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))

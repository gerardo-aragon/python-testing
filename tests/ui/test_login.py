import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.pages.login import LoginPage
from utils.database_helper import insert


@pytest.mark.usefixtures("driver_init")
class TestLogin:

    def test_login_admin(self):
        self.driver.get("http://localhost:4200/login")

        wait = WebDriverWait(self.driver, 5)
        login_page = LoginPage(self.driver)
        login_page.login("gerardoadmin", "Test123@")
        wait.until(EC.visibility_of_element_located((By.ID, "admins-import")))

    def test_invalid_login_admin(self):
        self.driver.get("http://localhost:4200/login")

        wait = WebDriverWait(self.driver, 5)
        login_page = LoginPage(self.driver)
        login_page.login("gerardoadmin", "Test123")
        wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))

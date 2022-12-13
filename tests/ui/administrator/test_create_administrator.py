import time
from src.pages.login.login import LoginPage
from src.pages.administrator.administrator_dashboard import AdministratorDashboard
import pytest

@pytest.mark.usefixtures('driver_init')
class TestCreateAdministrator:

    def test_create_administrator(self):
        self.driver.get("http://localhost:4200/login")

        login_page = LoginPage(self.driver)
        login_page.login("gerardoadmin", "Test123@")
        admin_dashboard = AdministratorDashboard(self.driver)
        admin_dashboard.click_create_admin_button()
        time.sleep(5)


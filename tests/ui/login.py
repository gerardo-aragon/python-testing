import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver_init")
class TestLogin:

    def test_login_admin(self):
        wait = WebDriverWait(self.driver, 3)
        self.driver.get("https://upre-fe-dev.vercel.app/")
        wait.until(EC.visibility_of_element_located((By.ID, "userName")))



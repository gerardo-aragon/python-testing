import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver_init(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver

    yield
    driver.close()

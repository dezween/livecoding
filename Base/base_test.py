import pytest

from Pages.login_page import LoginPage
from Pages.dashboard_page import DashboardPage
from Pages.personal_page import PersonalPage
from config.data import Data


class BaseTest:
    data = Data

    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_page: PersonalPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.personal_page = PersonalPage(driver)

import allure
from Base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(BasePage):
    PAGE_URL = Links.DASHBOARD_PAGE

    MY_INFO_BUTTON = ('xpath', '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span')

    @allure.step("Click on 'My Info' link")
    def click_my_info_link(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()

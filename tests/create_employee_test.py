import time

import allure
import pytest

from base.base_test import BaseTest



@allure.feature("PIM")
class TestCreateEmployee(BaseTest):

    @allure.title("Create new Employee")
    @allure.severity("Critical")
    @pytest.mark.regression
    def test_create_employee(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_pim_link()
        self.pim_page.is_opened()
        self.pim_page.create_new_employee()
        self.pim_page.enter_firstName(self.data.FIRST_NAME)
        self.pim_page.enter_lastName(self.data.LAST_NAME)
        self.pim_page.enter_employee_id(self.data.EMPLOYEE_ID)
        self.pim_page.click_save_button()
        self.pim_page.make_screenshot("New employee.png")
        self.dashboard_page.click_pim_link()
        self.pim_page.enter_employee_id(self.data.EMPLOYEE_ID)
        self.pim_page.click_search_button()
        self.pim_page.make_screenshot("Employee added.png")
        self.pim_page.check_search_result()
        self.pim_page.click_delete_button()
        self.pim_page.click_search_button()
        self.pim_page.check_delete_result()


import allure
import re
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

class PIMPage(BasePage):

    PAGE_URL = Links.PIM_PAGE

    ADD_BUTTON = ("xpath", "//button[normalize-space()='Add']")
    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    LAST_NAME_FIELD = ("xpath", "//input[@name='lastName']")
    EMPLOYEE_ID_FIELD = ("xpath", "//label[text()='Employee Id']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    SAVE_BUTTON = ("xpath", "//button[normalize-space()='Save']")
    SEARCH_BUTTON = ("xpath", "//button[normalize-space()='Search']")
    FOUND_LABEL = ("xpath", "//span[contains(@class, 'oxd-text') and contains(., 'Found')]")

    #SPINNER_LOADER = ("css selector", ".oxd-form-loader, .oxd-loading-spinner")

    DELETE_BUTTON = ("xpath", "//button[i[contains(@class,'bi-trash')]]")
    CONFIRMATION_DELETE_BUTTON = ("xpath", "//button[normalize-space()='Yes, Delete']")

    # def wait_for_loader_to_disappear(self):
    #     """Метод для ожидания исчезновения индикатора загрузки"""
    #     self.wait.until(EC.invisibility_of_element_located(self.SPINNER_LOADER))

    @allure.step("Create new employee")
    def create_new_employee(self):
        self.wait_for_loader_to_disappear()
        self.wait.until(EC.visibility_of_element_located(self.ADD_BUTTON)).click()

    @allure.step("Enter firstName")
    def enter_firstName(self, firstName):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD)).send_keys(firstName)

    @allure.step("Enter lastName")
    def enter_lastName(self, lastName):
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_FIELD)).send_keys(lastName)

    @allure.step("Enter the employeeID in the search field")
    def enter_employee_id(self, employeeId):
        employee_id_field = self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_ID_FIELD))
        employee_id_field.send_keys(Keys.CONTROL + "A")
        employee_id_field.send_keys(Keys.BACKSPACE)
        employee_id_field.send_keys(employeeId)

    @allure.step("Click save button")
    def click_save_button(self):
        self.wait_for_loader_to_disappear()
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Click search button")
    def click_search_button(self):
        self.wait_for_loader_to_disappear()
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

    @allure.step("Check that the employee has been added")
    def check_search_result(self):
        self.wait_for_loader_to_disappear()
        search_result = self.wait.until(EC.visibility_of_element_located(self.FOUND_LABEL))
        actual_text = search_result.text
        allure.attach(actual_text, name="Found Label Text", attachment_type=allure.attachment_type.TEXT)
        match = re.search(r"\d+", actual_text)
        if match:
            count = int(match.group())
        else:
            # Если цифр нет (NoneType), устанавливаем 0, чтобы сработал понятный assert
            count = 0

        assert count == 1, f"Expected 1 record, but found {count}. Text on screen: '{actual_text}'"

    @allure.step("Click delete button")
    def click_delete_button(self):
        self.wait_for_loader_to_disappear()
        self.wait.until(EC.element_to_be_clickable(self.DELETE_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.CONFIRMATION_DELETE_BUTTON)).click()

    @allure.step("Check that the employee has been deleted")
    def check_delete_result(self):
        self.wait_for_loader_to_disappear()
        search_result = self.wait.until(EC.visibility_of_element_located(self.FOUND_LABEL))
        actual_text = search_result.text
        allure.attach(actual_text, name="Found Label Text After Delete", attachment_type=allure.attachment_type.TEXT)
        match = re.search(r"\d+", actual_text)
        if match:
            count = int(match.group())
        else:
            count = 0

        assert count == 0, f"Expected 0 records (deleted), but found {count}. Text on screen: '{actual_text}'"




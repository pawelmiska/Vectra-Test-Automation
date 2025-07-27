from selenium.webdriver.common.by import By

class CheckoutStepOnePage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.zip_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

    def fill_customer_info(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.zip_input).send_keys(zip_code)

    def click_continue_button(self):
        self.driver.find_element(*self.continue_button).click()
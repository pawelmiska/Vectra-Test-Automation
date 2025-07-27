from selenium.webdriver.common.by import By

class CheckoutCompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.finish_button = (By.CLASS_NAME, "cart_button")
        self.confirmation_message = (By.CLASS_NAME, "complete-header")

    def click_finish_button(self):
        self.driver.find_element(*self.finish_button).click()

    def assert_order_confirmation(self):
        message = self.driver.find_element(*self.confirmation_message).text
        assert message == "Thank you for your order!", f"Expected confirmation message, got: '{message}'"

from selenium.webdriver.common.by import By
from decimal import Decimal

class CheckoutStepTwoPage:
    def __init__(self, driver):
        self.driver = driver
        self.summary_items = (By.CLASS_NAME, "cart_item")
        self.item_name = (By.CLASS_NAME, "inventory_item_name")
        self.item_price = (By.CLASS_NAME, "inventory_item_price")
        self.total_price = (By.CLASS_NAME, "summary_subtotal_label")

    def get_product_names(self):
        items = self.driver.find_elements(*self.summary_items)
        return [
            item.find_element(*self.item_name).text
            for item in items
        ]

    def get_total_price(self):
        items = self.driver.find_elements(*self.summary_items)
        prices = [
            Decimal(item.find_element(*self.item_price).text.replace("$", ""))
            for item in items
        ]
        return sum(prices)

    def assert_product_names(self, *expected_names):
        actual = self.get_product_names()
        assert sorted(actual) == sorted(expected_names), f"Expected {expected_names}, got {actual}"

    def assert_total_price(self):
        calculated = self.get_total_price()
        displayed = self.driver.find_element(*self.total_price).text
        displayed_value = Decimal(displayed.replace("Item total: $", ""))
        assert calculated == displayed_value, f"Expected ${calculated}, got ${displayed_value}"


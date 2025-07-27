from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.item_name = (By.CLASS_NAME, "inventory_item_name")
        self.checkout_button = (By.ID, "checkout")

    def get_product_names_in_cart(self):
        items = self.driver.find_elements(*self.cart_items)
        return [
            item.find_element(*self.item_name).text
            for item in items
        ]

    def assert_products_in_cart(self, *expected_names):
        actual_names = self.get_product_names_in_cart()
        assert sorted(actual_names) == sorted(expected_names), f"Expected {expected_names}, but got {actual_names}"

    def click_checkout_button(self):
        self.driver.find_element(*self.checkout_button).click()

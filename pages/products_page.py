from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.inventory_items = (By.CLASS_NAME, "inventory_item")
        self.item_name = (By.CLASS_NAME, "inventory_item_name")
        self.item_price = (By.CLASS_NAME, "inventory_item_price")
        self.add_to_cart_button = (By.CLASS_NAME, "btn_inventory")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def sort_by_price_low_to_high(self):
        dropdown = Select(self.driver.find_element(*self.sort_dropdown))
        dropdown.select_by_visible_text("Price (low to high)")

    def assert_products_sorted_by_price_ascending(self):
        items = self.driver.find_elements(*self.inventory_items)
        prices = [
            float(item.find_element(*self.item_price).text.replace("$", ""))
            for item in items
        ]
        assert prices == sorted(prices), f"Prices are not sorted ascending: {prices}"

    def add_first_product_to_cart(self):
        items = self.driver.find_elements(*self.inventory_items)
        items[0].find_element(*self.add_to_cart_button).click()

    def add_last_product_to_cart(self):
        items = self.driver.find_elements(*self.inventory_items)
        items[-1].find_element(*self.add_to_cart_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

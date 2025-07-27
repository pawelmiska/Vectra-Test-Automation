from utils.assertions import assert_url_contains
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage
import pytest

@pytest.mark.e2e
@pytest.mark.regression
def test_end_to_end_purchase(driver):
    products_page = ProductsPage(driver)
    checkout_page = CheckoutStepOnePage(driver)
    step_two = CheckoutStepTwoPage(driver)
    complete_page = CheckoutCompletePage(driver)
    cart_page = CartPage(driver)

    assert_url_contains(driver, "inventory")

    products_page.sort_by_price_low_to_high()
    products_page.assert_products_sorted_by_price_ascending()
    products_page.add_first_product_to_cart()
    products_page.add_last_product_to_cart()

    products_page.go_to_cart()

    cart_page.assert_products_in_cart("Sauce Labs Onesie","Sauce Labs Fleece Jacket")
    cart_page.click_checkout_button()

    checkout_page.fill_customer_info("Jan", "Kowalski", "12345")
    checkout_page.click_continue_button()

    step_two.assert_product_names("Sauce Labs Onesie", "Sauce Labs Fleece Jacket")
    step_two.assert_total_price()

    complete_page.click_finish_button()
    complete_page.assert_order_confirmation()




from .base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        button.click()

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), \
        'button "add to busket" is not presented'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        'Success message does not disappeared'

    def should_add_to_basket(self):
        self.should_same_name()
        self.should_same_price()
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), \
        'there is no message about adding to cart'

    def should_same_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FORM).text
        added_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert name == added_name, 'the name of the added product does not match'

    def should_same_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_FORM).text
        added_price = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_PRICE_FORM).text
        assert price == added_price, 'the price of the added product does not match'
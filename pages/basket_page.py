from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
        "There are products in the basket, but should not be"

    def should_be_basket_is_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_FORM), \
        'basket is empty text is not presented'
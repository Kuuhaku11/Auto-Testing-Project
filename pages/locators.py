from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, 'login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, '#messages :first-child')
    PRODUCT_NAME_FORM = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_ADD_NAME_FORM = (By.CSS_SELECTOR, '#messages :first-child strong')
    PRODUCT_PRICE_FORM = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_ADD_PRICE_FORM = (By.CSS_SELECTOR, '#messages :nth-child(3) strong')

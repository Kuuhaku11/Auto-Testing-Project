from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.ID, 'login_link')
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    PROFILE_LINK = (By.CSS_SELECTOR, '.navbar-right :first-child a')


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items :nth-child(1).row')
    BASKET_IS_EMPTY_FORM = (By.CSS_SELECTOR, '#content_inner p:first-child')


class DeleteProfileLocators():
    DELETE_PROFILE_PASSWORD_FORM = (By.ID, 'id_password')
    DELETE_BUTTON = (By.CLASS_NAME, 'btn-danger')

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTRATION_EMAIL_FORM = (By.NAME, 'registration-email')
    REGISTRATION_PASSWORD_FORM = (By.NAME, 'registration-password1')
    REGISTRATION_CONFIRM_PASSWORD_FORM = (By.NAME, 'registration-password2')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')


class MainPageLocators():
    LOGIN_LINK = (By.ID, 'login_link')


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, '#messages :first-child')
    PRODUCT_NAME_FORM = (By.CSS_SELECTOR, '.product_main h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages :first-child strong')
    PRODUCT_PRICE_FORM = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_ADD_PRICE_FORM = (By.CSS_SELECTOR, '#messages :nth-child(3) strong')


class ProfilePageLocators():
    DELETE_PROFILE = (By.ID, 'delete_profile')
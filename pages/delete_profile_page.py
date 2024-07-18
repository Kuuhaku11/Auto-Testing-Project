from .base_page import BasePage
from pages.locators import DeleteProfileLocators


class DeleteProfilePage(BasePage):
    def delete(self, password):
        self.browser.find_element(*DeleteProfileLocators.DELETE_PROFILE_PASSWORD_FORM).send_keys(password)
        self.browser.find_element(*DeleteProfileLocators.DELETE_BUTTON).click()
        
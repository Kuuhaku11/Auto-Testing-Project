from .base_page import BasePage
from .delete_profile_page import DeleteProfilePage
from pages.locators import ProfilePageLocators


class ProfilePage(BasePage):
    def delete_profile(self, password):
        link = self.browser.find_element(*ProfilePageLocators.DELETE_PROFILE)
        link.click()
        delete_profile_page = DeleteProfilePage(self.browser, self.browser.current_url)
        delete_profile_page.delete(password)


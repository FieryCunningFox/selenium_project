from .base_page import BasePage
from selenium import webdriver
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_link = self.browser.current_url
        index = current_link.find("login")
        assert index != -1, f"Expected 'login' is substring of '{current_link}'"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "No login form"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "No register form"
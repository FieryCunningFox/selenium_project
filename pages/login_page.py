from .base_page import BasePage
from selenium import webdriver
from .locators import LoginPageLocators, BasePageLocators
import pytest
import time


class LoginPage(BasePage):
    def fill_login_form(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        password_field = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        email_field.send_keys(email)
        password_field.send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        print("LOGIN is succussful!")
        
    def fill_registration_form(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_repeat_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_repeat_password.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        print("REGISTER is successful!")
    
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
        
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"
from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_be_empty_busket(self):
        busket_message = self.browser.find_element(*BasketPageLocators.BUSKET_MESSAGE).text
        expected_message = "Your basket is empty. Continue shopping"
        assert busket_message == expected_message, "Busket is not empty, but should be"
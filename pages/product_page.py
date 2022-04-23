from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def push_button(self):
        try:
            self.browser.find_element(*ProductPageLocators.BUTTON_ADD).click()
        except NoSuchElementException:
            return "Button added product to busket not found"
        
    def go_to_basket(self):
        button_busket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_busket.click()
        
    def should_be_added_to_basket(self):
        self.solve_quiz_and_get_code()
        self.should_price_basket_be_similar_to_product()
        self.should_name_in_message_be_similar_to_product()
        
        
    def should_price_basket_be_similar_to_product(self):
        price_busket = self.browser.find_element(*ProductPageLocators.PRICE_BUSKET).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE).text
        print("Product price: ", price_product, "Busket price: ", price_busket)
        assert price_busket == price_product, "Price of product are not similar"
        
    def should_name_in_message_be_similar_to_product(self):
        name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_IN_BUSKET).text
        message_expected = f"{name} has been added to your basket."
        print("Product name: ", name, "Message: ", message)
        assert message_expected == message, "Name in message is wrong"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        
    def should_not_be_success_message_2(self):
        result = self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
        assert result == True, "Success message is presented, but should not be"
    
    
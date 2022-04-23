from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from .locators import ProductPageLocators
import time

class ProductPage(BasePage): 
    def should_be_added_to_basket(self):
        try:
            self.is_element_present(*ProductPageLocators.NAME_PRODUCT)
            name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        except NoSuchElementException:
            return "Name not found"
            
        try:
            self.browser.find_element(*ProductPageLocators.BUTTON_ADD).click()
        except NoSuchElementException:
            return "Button added product to busket not found"
            
        self.solve_quiz_and_get_code()
        
        try:
            self.is_element_present(*ProductPageLocators.MESSAGE_BUSKET_STATUS)
            message_status = self.browser.find_element(*ProductPageLocators.MESSAGE_BUSKET_STATUS).text
            index = message_status.find("In stock")
            assert index != -1, "Product was not added to busket, message status is invalid"
        except NoSuchElementException:
            return "Message status object not found"
        
        try:
            self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_IN_BUSKET)
            message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_IN_BUSKET).text
            index = message.find(name)
            assert index != -1, "Message after adding product to busket is invalid"
        except NoSuchElementException:
            return "Message after adding product not found"
        
        try:
            self.is_element_present(*ProductPageLocators.PRICE)
            price_product = self.browser.find_element(*ProductPageLocators.PRICE).text
        except NoSuchElementException:
            return "Price of product not found"
        
        try:
            self.is_element_present(*ProductPageLocators.PRICE_BUSKET)
            price_busket = self.browser.find_element(*ProductPageLocators.PRICE_BUSKET).text
        except NoSuchElementException:
            return "Message about price of busket not found"
        
        assert price_busket == price_product, f"Price of product = {price_product}, but price of busket = {price_busket}"

    
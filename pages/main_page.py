from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
        
    def go_to_basket(self):
        button_busket = self.browser.find_element(*MainPageLocators.BUTTON_BASKET)
        button_busket.click()
        
    

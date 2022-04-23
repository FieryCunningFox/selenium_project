from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    

class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, "button[value='Add to basket']")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main")
    MESSAGE_BUSKET_STATUS = (By.CSS_SELECTOR, ".instock availability")
    MESSAGE_PRODUCT_IN_BUSKET = (By.CSS_SELECTOR, ".alertinner")
    PRICE  = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_BUSKET = (By.CSS_SELECTOR, ".alertinner strong")
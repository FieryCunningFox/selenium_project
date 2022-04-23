from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class MainPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    

class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, "button[value='Add to basket']")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")
    MESSAGE_PRODUCT_IN_BUSKET = (By.CSS_SELECTOR, ".alertinner")
    PRICE  = (By.CSS_SELECTOR, "p.price_color")
    PRICE_BUSKET = (By.CSS_SELECTOR, "#messages .alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1)")
    BUTTON_BASKET = (By.CSS_SELECTOR, ".basket-mini span.btn-group a.btn.btn-default")
    
class BasketPageLocators():
    BUSKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
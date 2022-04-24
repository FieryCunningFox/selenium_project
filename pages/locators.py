from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    

class MainPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")
    

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
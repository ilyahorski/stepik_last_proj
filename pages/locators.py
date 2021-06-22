from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CLASS_NAME, 'btn btn-default dropdown-toggle')


class LoginPageLocators():
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_BTN = (By.NAME, "login_submit")

    REG_EMAIL = (By.ID, "id_registration-email")
    REG_PASSWORD = (By.ID, "id_registration-password1")
    REG_REPEAT_PAS = (By.ID, "id_registration-password2")
    REG_BTN = (By.NAME, "registration_submit")


class ProductPageLocators():
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    BASKET_STRONG_NAMES = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_ADD_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success:nth-child(1)")
    BASKET_LINK = (By.CLASS_NAME, 'btn btn-default dropdown-toggle')


class BasePageLocators():
    LOGIN_LINK = (By.ID, 'login_link')
    LOGIN_LINK_INVALID = (By.ID, 'login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, 'span .btn-default:nth-child(1)')


class BasketPageLocators():
    BASKET_EMPTY_TEXT = (By.ID, 'content_inner')



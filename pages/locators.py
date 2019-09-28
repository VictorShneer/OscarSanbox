from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, "#messages")
    ALERT_INFO = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_ADDED_ALERT = (By.CSS_SELECTOR, "#messages :nth-child(2)")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

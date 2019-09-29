from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_BUTTON          = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE               = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGES    = (By.CSS_SELECTOR, "#messages")
    ALERT_INFO          = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_ADDED_ALERT = (By.CSS_SELECTOR, "#messages :nth-child(2)")
    PRODUCT_TITLE       = (By.CSS_SELECTOR, ".product_main h1")


class BasePageLocators():
    LOGIN_LINK         = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET        = (By.CSS_SELECTOR, "body > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
	ITEMS_CONTAINER    = (By.CSS_SELECTOR, '.basket-items')
	EMPTY_BASKET_TEXT  = (By.CSS_SELECTOR, '#content_inner p')


class LoginPageLocators():
	EMAIL_REG_FIELD         = (By.CSS_SELECTOR, '#id_registration-email')
	PASSWORD_REG_FIELD      = (By.CSS_SELECTOR, '#id_registration-password1')
	PASSWORD_REG_CONF_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
	REG_BUTTON              = (By.CSS_SELECTOR, "[name='registration_submit']")
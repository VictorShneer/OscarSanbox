import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time

PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
LOGIN_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
    	email = str(time.time()) + "@fakemail.org"

    	login_page = LoginPage(browser, LOGIN_LINK)
    	login_page.open()
    	login_page.register_new_user(email,'UnBreakablePassw0rd')
    	login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        product_page = ProductPage(browser, PRODUCT_LINK)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        product_page = ProductPage(browser, PRODUCT_LINK)
        product_page.open()
        product_page.add_to_cart()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_product_title()
        product_page.should_be_price()
        product_page.should_be_success_messages()
        product_page.should_be_alert_info()
        product_page.should_be_product_added_alert()
        product_page.should_be_product_title_in_product_added_alert()
        product_page.should_basket_price_be_equal_to_product_price()
    


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_title()
    product_page.should_be_price()
    product_page.should_be_success_messages()
    product_page.should_be_alert_info()
    product_page.should_be_product_added_alert()
    product_page.should_be_product_title_in_product_added_alert()
    product_page.should_basket_price_be_equal_to_product_price()
    



@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, PRODUCT_LINK)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_not_be_success_message()



def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, PRODUCT_LINK)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, PRODUCT_LINK)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_success_message_to_dissapear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()



@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.open()
    basket_page.should_not_be_items()
    basket_page.should_be_empty_basket_text()

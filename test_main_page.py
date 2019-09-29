import pytest
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage



def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/'
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.open()
    basket_page.should_not_be_items()
    basket_page.should_be_empty_basket_text()
from .locators import ProductPageLocators
from .base_page import BasePage



class ProductPage(BasePage):

    SECOND_PART_OF_SUCCESS_MESSAGE = " has been added to your basket."

    def add_to_cart(self):
	    add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
	    add_to_cart_button.click()

    
    def should_be_price(self):
    	assert self.is_element_present(*ProductPageLocators.PRICE), "There is no price at product page."
    def should_be_success_messages(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "There are no success messages"
    def should_be_alert_info(self):
    	assert self.is_element_present(*ProductPageLocators.ALERT_INFO), "There is no alert info"
    def should_be_product_title(self):
    	assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE), 'There is no product title'
    def should_be_product_added_alert(self):
    	assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_ALERT), 'There is no product added alert'



    def should_be_product_title_in_product_added_alert(self):
        product_title = self.get_product_title()
        product_added_alert = self.get_product_added_alert()
        assert product_title + self.SECOND_PART_OF_SUCCESS_MESSAGE == product_added_alert,\
         'Product added alert is wrong.\n Alert: {}\nTitle: {}'.format(product_added_alert,product_title)
    
    def should_basket_price_be_equal_to_product_price(self):
    	price = self.get_price()
    	basket_value = self.get_basket_value_from_alert_info()
    	assert price == basket_value, "Basket value is not equal to produst price"
    


    def get_price(self):
	    price = self.browser.find_element(*ProductPageLocators.PRICE).text
	    return price
    def get_basket_value_from_alert_info(self):
    	return self.browser.find_element(*ProductPageLocators.ALERT_INFO).text    	
    def get_product_title(self):
    	return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
    def get_product_added_alert(self):
    	return self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_ALERT).text


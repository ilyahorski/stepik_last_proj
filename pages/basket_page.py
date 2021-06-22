from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_item_not_in_basket(self):
        self.basket_empty_text()

    def basket_empty_text(self):
        basket_empty_text = self.browser.find_elements(*BasketPageLocators.BASKET_EMPTY_TEXT)
        assert basket_empty_text, "Basket not empty"
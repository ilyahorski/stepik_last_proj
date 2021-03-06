from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


# def test_guest_can_go_to_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()  # открываем страницу
#     page.should_be_login_link()
#
#
# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com"
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()
#     login_page.should_be_register_form()
#
#
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_empty_text()

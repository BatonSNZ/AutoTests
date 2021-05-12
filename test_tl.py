from os import link
from .main_page import MainPage
def test_go_to_login_page(browser):
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()
    page.should_be_start_page()
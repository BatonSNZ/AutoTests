from os import link
from .main_page import MainPage
import pytest

def test_go_to_login_page(browser):
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()             #Авторизация на портале
    page.should_be_start_page()    #Проверка автризации

def test_go_to_tl(browser):
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.open_tl()                 #Открытие TL
    page.check_open_tl()           #Проверка отрытия TL 

@pytest.mark.work
def test_create_new_event(browser):
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.open_tl()                #Открытие TL
    page.check_open_tl()          #Проверка отрытия TL
    page.new_event_in_tl()        #Создание события Шаблон Шаблоныч через кнопку создать событие
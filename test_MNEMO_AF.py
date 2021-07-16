from .main_page_MNEMO import MainPageMNEMO
import pytest

def test_go_to_login_page(browser): # Авторизация на портале
    link = "http://192.168.36.28:8093"
    page = MainPageMNEMO(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации


def test_go_to_mnemo(browser): # Открытие мнемосхемы с value
    link = "http://192.168.36.28:8093"
    page = MainPageMNEMO(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_mnemo()                                               #Открытие мнемосхемы с value


def test_check_value(browser): # Проверка значений value
    link = "http://192.168.36.28:8093"
    page = MainPageMNEMO(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_mnemo()                                               #Открытие мнемосхемы с value
    page.check_value_load()                                         #Проверка загрузки значений value
    page.check_value()                                              #Проверка значений value


def test_check_smart_trend(browser): # Проверка Smart Trend
    link = "http://192.168.36.28:8093"
    page = MainPageMNEMO(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_mnemo()                                               #Открытие мнемосхемы с value
    page.check_value_load()                                         #Проверка загрузки значений value
    page.check_smart_trend()                                        #Проверка Smart Trend
    page.full_screan_smart_trend()                                  #Открытие Smart Trend на полный экран

@pytest.mark.work
def test_check_new_graph(browser): # Проверка Новый график
    link = "http://192.168.36.28:8093"
    page = MainPageMNEMO(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_mnemo()                                               #Открытие мнемосхемы с value
    page.check_value_load()                                         #Проверка загрузки значений value
    page.check_new_graph()                                          #Проверка Новый график  





    
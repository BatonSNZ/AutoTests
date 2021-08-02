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


def test_check_new_graph(browser): # Проверка Новый график
    link = "http://192.168.36.28:8093"
    page = MainPageMNEMO(browser, link)
    page.open()     
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_mnemo()                                               #Открытие мнемосхемы с value
    page.check_value_load()                                         #Проверка загрузки значений value
    page.check_new_graph()                                          #Проверка Новый график  


def test_check_simple_trend(browser): # Проверка Простой тренд
    link = "http://192.168.36.28:8093"
    page = MainPageMNEMO(browser, link)
    page.open()     
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_mnemo()                                               #Открытие мнемосхемы с value
    page.check_value_load()                                         #Проверка загрузки значений value
    page.simple_trend()                                             #Проверка Простой тренд


def test_check_bar(browser): # Проверка Бара
    link = "http://192.168.36.28:8093"
    page = MainPageMNEMO(browser, link)
    page.open()     
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_mnemo()                                               #Открытие мнемосхемы с value
    page.check_value_load()                                         #Проверка загрузки значений value
    page.check_bar()                                                #Проверка Баров


def test_check_table(browser): # Выгрузка в таблицу
    link = "http://192.168.36.28:8093"
    page = MainPageMNEMO(browser, link)
    page.open()     
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_mnemo()                                               #Открытие мнемосхемы с value
    page.check_value_load()                                         #Проверка загрузки значений value
    page.table_from_select_param()                                  #Выгрузка в таблицу через Выбор параметров
    page.table_from_smart_trend()                                   #Выгрузка в таблицу через SmartTrend 
    page.table_from_new_graf()                                      #Выгрузка в таблицу через Новый график   

@pytest.mark.work
def test_zone_makers(browser): # Проверка работы ZoneMakers    
    link = "http://192.168.36.28:8093"
    page = MainPageMNEMO(browser, link)
    page.open()     
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_mnemo_zonemaker()                                     #Открытие мнемосхемы с ZoneMakers
    page.check_zone_maker_setings_visio()                           #Проверка работы ZoneMaker с настройками Visio
    page.check_zone_maker_setings_portal()                          #Проверка работы ZoneMaker с настройками Портала



    
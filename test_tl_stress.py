from .main_page import MainPage
import pytest

def test_go_to_tl1(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl2(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl3(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl4(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl5(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl6(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl7(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl8(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl9(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl10(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl11(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl12(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl13(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl14(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl15(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl16(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl17(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl18(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl19(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl20(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl21(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl22(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl23(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl24(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl25(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl26(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl27(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl28(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl29(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

def test_go_to_tl30(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 
    page.changes_time_tl()                                          #Изменение временого диапазона
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов        





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

def test_create_new_event_button(browser):
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.open_tl()                                         #Открытие TL
    page.check_open_tl()                                   #Проверка отрытия TL
    page.open_create_new_event_shablon_shablonich()        #Открытие крточки нового события Шаблон Шаблоныч через кнопку "Создать событие"
    page.enter_data_into_event_shablon_shablonich()        #Заполнение карточки события Шаблон Шаблоныч

def test_create_new_event_menu(browser):
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL
    page.new_event_in_tl_from_menu()                                #Создание события Шаблон Шаблоныч через меню
    page.enter_data_into_event_shablon_shablonich_no_work_center()  #Заполнение карточки события Шаблон Шаблоныч после открытия через меню


def test_auto_open_menu(browser):
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL
    page.new_event_in_tl_from_menu()                                #Открытие карточки события Шаблон Шаблоныч через меню
    page.check_auto_open_menu()                                     #Проверка втораскрытия меню

@pytest.mark.work
def test_change_event(browser):
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL
    page.new_event_in_tl_from_menu()                                #Создание события Шаблон Шаблоныч через меню
    page.enter_data_into_event_shablon_shablonich_no_work_center()  #Заполнение карточки события Шаблон Шаблоныч после открытия через меню
    page.refresh_page()                                             #Обновление страницы
    page.open_event_frame()                                         #Открытие карточки события
    page.change_event_frame()                                       #Внесение изменений в событие
    



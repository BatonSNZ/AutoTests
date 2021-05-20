from .main_page import MainPage
import pytest

def test_go_to_login_page(browser): # Авторизация на портале
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации

def test_go_to_tl(browser): # Вход в журнал TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL 

def test_create_new_event_button(browser): # Создание события в журнале TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL
    page.open_create_new_event_shablon_shablonich()                 #Открытие крточки нового события Шаблон Шаблоныч через кнопку "Создать событие"
    page.enter_data_into_event_shablon_shablonich()                 #Заполнение карточки события Шаблон Шаблоныч

def test_create_new_event_menu(browser): # Создание события через элемент структурной модели
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL
    page.new_event_in_tl_from_menu()                                #Создание события Шаблон Шаблоныч через меню
    page.enter_data_into_event_shablon_shablonich_no_work_center()  #Заполнение карточки события Шаблон Шаблоныч после открытия через меню


def test_auto_open_menu(browser): # Раскрытие структуры данных до выбранного элемента
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL
    page.new_event_in_tl_from_menu()                                #Открытие карточки события Шаблон Шаблоныч через меню
    page.check_auto_open_menu()                                     #Проверка втораскрытия меню

def test_change_event(browser): # Редактирование события в журнале TL и вкладка История
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
    page.refresh_page()                                             #Обновление страницы
    page.open_event_frame()                                         #Открытие карточки события
    page.check_change_in_event()                                    #Проверка изменений на вкладке История

def test_create_attach_event(browser): # Создание вложенного события и вкладка Связи
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL
    page.new_event_in_tl_from_menu()                                #Создание события Шаблон Шаблоныч через меню
    page.enter_data_into_event_shablon_shablonich_no_work_center()  #Заполнение карточки события Шаблон Шаблоныч после открытия через меню
    page.refresh_page()                                             #Обновление страницы
    page.create_attach_event()                                      #Открытие окна регистрации вложенного события
    page.enter_data_into_event_prostoi_oborudovania()               #Заполнение карточки события Простой оборудования
    page.refresh_page()                                             #Обновление страницы
    page.check_attach_event_create()                                #Проверка создания вложенного события
    
def test_add_investments(browser): # Добавление вложения и вкладка Вложения
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL
    page.new_event_in_tl_from_menu()                                #Создание события Шаблон Шаблоныч через меню
    page.enter_data_into_event_shablon_shablonich_no_work_center()  #Заполнение карточки события Шаблон Шаблоныч после открытия через меню
    page.refresh_page()                                             #Обновление страницы
    page.add_investments()                                          #Добавление файла
    page.refresh_page()                                             #Обновление страницы
    page.check_investments()                                        #проверка добавления файла

def test_delete_event(browser): # Удаление события в журнале TL
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL
    page.new_event_in_tl_from_menu()                                #Создание события Шаблон Шаблоныч через меню
    page.enter_data_into_event_shablon_shablonich_no_work_center()  #Заполнение карточки события Шаблон Шаблоныч после открытия через меню
    page.refresh_page()                                             #Обновление страницы
    page.delete_event_checkbox()                                    #Удаление события через чекбокс
    page.refresh_page()                                             #Обновление страницы
    page.new_event_in_tl_from_menu()                                #Создание события Шаблон Шаблоныч через меню
    page.enter_data_into_event_shablon_shablonich_no_work_center()  #Заполнение карточки события Шаблон Шаблоныч после открытия через меню
    page.refresh_page()                                             #Обновление страницы
    page.delete_event()                                             #Удаление события через карточку события

def test_filter_menu(browser): # Фильтрация событий по группе объектов
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.open_tl()                                                  #Открытие TL
    page.check_open_tl()                                            #Проверка отрытия TL
    page.filter_even_menu()                                         #Фильтрация событий по группе объектов
    page.check_filter_event_menu()                                  #Проверка фильтрации по группе объектов

@pytest.mark.work
def test_pages(browser):
    link = "http://192.168.36.28:8093"
    page = MainPage(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_settings()                                            #Открытие натроек TL
    page.changing_number_events()                                   #Изменение колличества событий на странице журнала TL



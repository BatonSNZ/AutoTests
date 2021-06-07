from .main_page_PMM import MainPagePMM
import pytest

def test_go_to_login_page(browser): # Авторизация на портале
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации


def test_go_to_pmm(browser): # Вход в журнал PMM
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_pmm()                                                 #Открытие PMM
    page.select_predstavlenie()                                     #Выбор режима
    page.check_open_pmm()                                           #Проверка отрытия PMM     


def test_open_event(browser): # Открытие карточки события
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_pmm()                                                 #Открытие PMM
    page.select_predstavlenie()                                     #Выбор режима
    page.check_open_pmm()                                           #Проверка отрытия PMM 
    page.open_event()                                               #Открытие карточки события
    page.check_open_event()                                         #Проверка открытия карточки события    


def test_kvitirovanie(browser): # Квитирование события
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_pmm()                                                 #Открытие PMM
    page.select_predstavlenie()                                     #Выбор режима
    page.check_open_pmm()                                           #Проверка отрытия PMM 
    page.open_event()                                               #Открытие карточки события
    page.check_open_event()                                         #Проверка открытия карточки события 
    page.press_button_kvit()                                        #Квитирование и закрытие карточки события
    page.refresh_page()                                             #Обновление страницы 
    page.check_kvit()                                               #Проверка в журнале событий  

@pytest.mark.work
def test_kvitirovanie(browser): # Добавление комментария
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_pmm()                                                 #Открытие PMM
    page.select_predstavlenie()                                     #Выбор режима
    page.check_open_pmm()                                           #Проверка отрытия PMM 
    page.open_event()                                               #Открытие карточки события
    page.check_open_event()                                         #Проверка открытия карточки события 
    page.add_comment()                                              #Добавление коммента
    page.refresh_page()                                             #Обновление страницы
    page.check_comment()                                            #Проверка комментария в журнале





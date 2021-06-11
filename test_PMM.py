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

 
def test_kvit(browser): # Квитирование события
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
    page.check_open_pmm()                                           #Проверка отрытия PMM 
    page.check_kvit()                                               #Проверка в журнале событий    


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


def test_recomend(browser): # Вкладка Рекомендации
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
    page.select_recomend()                                          #Выбор действий во вкладке Рекомендации
    page.refresh_page()                                             #Обновление страницы
    page.check_open_pmm()                                           #Проверка отрытия PMM 
    page.open_event()                                               #Открытие карточки события
    page.check_open_event()                                         #Проверка открытия карточки события
    page.check_save_recomend()                                      #Проверка сохранения изменений во вкладке Рекомендации 


def test_trend(browser): # Вкладка Тренд
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
    page.open_tab_trend()                                           #Открытие вкладки Тренд
    page.select_trend()                                             #Выбор Тренд отклонения вверх
    #page.check_trend()                                              #Прверка тренда


def test_doc(browser): # Вкладка Документы
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
    page.open_tab_doc()                                             #Открытие вкладки Документы
    page.add_doc()                                                  #Добавление документа
    page.refresh_page()                                             #Обновление страницы
    page.check_open_pmm()                                           #Проверка отрытия PMM 
    page.open_event()                                               #Открытие карточки события
    page.check_open_event()                                         #Проверка открытия карточки события
    page.open_tab_doc()                                             #Открытие вкладки Документы
    page.check_doc()                                                #Проверка наличия нового документа после обновления страницы 


def test_statistika(browser): # Вкладка Статистика
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
    page.open_tab_stat()                                            #Открытие вкладки Статистика

@pytest.mark.work
def test_filtrs(browser): # Фильтры "Активны", "Завершены", "Квитированные" и "Неквитированные"
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_pmm()                                                 #Открытие PMM
    page.select_predstavlenie()                                     #Выбор режима
    page.check_open_pmm()                                           #Проверка отрытия PMM 
    page.filter()                                                   #Фильтрация



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

@pytest.mark.work
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


def test_filter_for_model_proizvodsva(browser): # Фильтрация по модели производства
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_pmm()                                                 #Открытие PMM
    page.select_predstavlenie()                                     #Выбор режима
    page.check_open_pmm()                                           #Проверка отрытия PMM    
    page.filter_for_model_proizvodsva()                             #Фильтрация по модели производства


def test_check_rights(browser): # Проверка прав доступа в PMM
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login_sokol()                                        #Авторизация на портале за sokol
    page.should_be_start_page()                                     #Проверка автризации
    page.check_limit_rights_on_start_page()                         #Проверка ограничений прав на главной странице
    page.open_pmm()                                                 #Открытие PMM
    page.select_predstavlenie()                                     #Выбор режима
    page.check_open_pmm()                                           #Проверка отрытия PMM 
    page.check_rights_PMM()                                         #Проверка ограничения прав доступа в PMM


def test_filter_for_time(browser): # Фильтрация по времени
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_pmm()                                                 #Открытие PMM
    page.select_predstavlenie()                                     #Выбор режима
    page.check_open_pmm()                                           #Проверка отрытия PMM
    page.time_filter()                                              #Фильтрация по времени в журнале PMM


def test_change_namder_event_page(browser): # Изменение количества событий на странице
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_pmm()                                                 #Открытие PMM
    page.select_predstavlenie()                                     #Выбор режима
    page.check_open_pmm()                                           #Проверка отрытия PMM
    page.change_namder_event()                                      #Изменение чилса событий на странице
    page.change_namber_event_after_test()                           #Возвращение 20 событий на странице


def test_sort_event(browser): # Сортировака событий в настройках
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_pmm()                                                 #Открытие PMM
    page.select_predstavlenie()                                     #Выбор режима
    page.check_open_pmm()                                           #Проверка отрытия PMM
    page.sort_kvit()                                                #Фильтрация по признаку квитирования
    page.sort_status()                                              #Фильтрация по статусу события
    page.sort_time()                                                #Фильтрация по времени начала
    page.change_namber_event_after_test()                           #Вернуть количество страниц





def test_filtrs_act_cvit(browser): # Фильтрация по "Активны" + "Квитированные" 
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_pmm()                                                 #Открытие PMM
    page.select_predstavlenie()                                     #Выбор режима
    page.check_open_pmm()                                           #Проверка отрытия PMM 
    page.filter_act_cvit()                                          #Фильтрация по "Активны" + "Квитированные"


def test_filtrs_act_nocvit(browser): # Фильтрация по "Активны" + "Неквитированные"
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_pmm()                                                 #Открытие PMM
    page.select_predstavlenie()                                     #Выбор режима
    page.check_open_pmm()                                           #Проверка отрытия PMM 
    page.filter_act_nocvit()                                        #Фильтрация по "Активны" + "Неквитированные"


def test_filtrs_noact_cvit(browser): # Фильтрация по "Завершены" + "Квитированные" 
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_pmm()                                                 #Открытие PMM
    page.select_predstavlenie()                                     #Выбор режима
    page.check_open_pmm()                                           #Проверка отрытия PMM 
    page.filter_noact_cvit()                                        #Фильтрация по "Завершены" + "Квитированные"    


def test_filtrs_noact_nocvit(browser): # Фильтрация по "Завершены" + "Неквитированные"
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_pmm()                                                 #Открытие PMM
    page.select_predstavlenie()                                     #Выбор режима
    page.check_open_pmm()                                           #Проверка отрытия PMM 
    page.filter_noact_nocvit()                                      #Фильтрация по "Завершены" + "Неквитированные"


def test_filters_cvit_act(browser): # Фильтрация по "Квитированные" + "Активны" 
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_pmm()                                                 #Открытие PMM
    page.select_predstavlenie()                                     #Выбор режима
    page.check_open_pmm()                                           #Проверка отрытия PMM 
    page.filter_cvit_act()                                          #Фильтрация по "Квитированные" + "Активны"


def test_filters_cvit_noact(browser): # Фильтрация по "Квитированные" + "Завершены" 
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_pmm()                                                 #Открытие PMM
    page.select_predstavlenie()                                     #Выбор режима
    page.check_open_pmm()                                           #Проверка отрытия PMM 
    page.filter_cvit_noact()                                        #Фильтрация по "Квитированные" + "Завершены"    


def test_filters_nocvit_act(browser): # Фильтрация по "Неквитированные" + "Активны" 
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_pmm()                                                 #Открытие PMM
    page.select_predstavlenie()                                     #Выбор режима
    page.check_open_pmm()                                           #Проверка отрытия PMM 
    page.filter_nocvit_act()                                        #Фильтрация по "Неквитированные" + "Активны" 


def test_filters_nocvit_noact(browser): # Фильтрация по "Неквитированные" + "Завершены" 
    link = "http://192.168.36.28:8093"
    page = MainPagePMM(browser, link)
    page.open()
    page.in_to_login()                                              #Авторизация на портале
    page.should_be_start_page()                                     #Проверка автризации
    page.open_pmm()                                                 #Открытие PMM
    page.select_predstavlenie()                                     #Выбор режима
    page.check_open_pmm()                                           #Проверка отрытия PMM 
    page.filter_nocvit_noact()                                      #Фильтрация по "Неквитированные" + "Завершены"          




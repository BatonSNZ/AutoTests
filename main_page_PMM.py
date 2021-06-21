from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class MainPagePMM(BasePage):
    def in_to_login(self): #Авторизация sam
        username_fild = self.browser.find_element(By.ID, 'txtUserName')
        username_fild.clear()
        username_fild.send_keys("sam")
        password_fild = self.browser.find_element(By.ID, 'txtPassword')
        password_fild.clear()
        password_fild.send_keys("sam")
        enter_button = self.browser.find_element(By.CLASS_NAME, 'btn-login')
        enter_button.click()

    def in_to_login_dev(self): #Авторизация dev
        username_fild = self.browser.find_element(By.ID, 'txtUserName')
        username_fild.clear()
        username_fild.send_keys("dev\\dev")
        password_fild = self.browser.find_element(By.ID, 'txtPassword')
        password_fild.clear()
        password_fild.send_keys("Gfhjkm123")
        enter_button = self.browser.find_element(By.CLASS_NAME, 'btn-login')
        enter_button.click()

    def in_to_login_sokol(self): #Авторизация sokol
        username_fild = self.browser.find_element(By.ID, 'txtUserName')
        username_fild.clear()
        username_fild.send_keys("sokol")
        password_fild = self.browser.find_element(By.ID, 'txtPassword')
        password_fild.clear()
        password_fild.send_keys("sokol")
        enter_button = self.browser.find_element(By.CLASS_NAME, 'btn-login')
        enter_button.click()     

    def should_be_start_page(self): #Проверка аторизации
        assert self.is_element_present(By.XPATH, '//a[text()="KTP"]'), "Не авторизовался" 

    def check_limit_rights_on_start_page(self): # Проверка ограничений прав на главной странице
        assert self.is_element_no_present(By.XPATH, '//a[text()="Bugs"]'), "Не работают ограничения прав доступа на главной странице"       

    def open_pmm(self): #Открытие PMM       
        pmm_button = self.browser.find_element(By.XPATH, '//a[text()="KTP"]')
        pmm_button.click()

    def select_predstavlenie(self): # Выбор представления
        select_operativ_jornal = self.browser.find_element(By.XPATH, '//span[text()="Режим оперативного журнала"]')
        select_operativ_jornal.click()
        button_select = self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]')    
        button_select.click()

    def check_open_pmm(self): # Проверка открытия PMM        
        assert self.is_element_present_with_waiting(By.XPATH, '//span[text()="Неквитированные"]'), "Нет кнопки неквитировано"
        assert self.is_element_present_with_waiting(By.CSS_SELECTOR, '[style="background: rgb(255, 216, 0);"'), "Нет событий в PMM"

    def open_event(self): # Открытие карточки события
        event = self.browser.find_element(By.CSS_SELECTOR, '[style="background: rgb(255, 216, 0);"')
        self.double_click(event)    

    def check_open_event(self): # Проверка откытия карточки события
        assert self.is_element_present_with_waiting(By.CSS_SELECTOR, '[ng-click="updateEvent(eventIds)"]') and self.is_element_present_with_waiting(By.XPATH, '//span[text()="Значение пробития границы: "]'), "Карточка события не открывается"

    def press_button_kvit(self): # Нажать на кнопку Квитировать
        button_kvit_or_close = self.browser.find_element(By.CSS_SELECTOR, '[ng-click="updateEvent(eventIds)"]')
        button_kvit_or_close.click()
        assert self.is_element_present_with_waiting(By.CSS_SELECTOR, '[class="popup__button js-confirm-btn ng-binding popup__top-info-button-disable"]'), 'Кнопка Квитировать активна'
        button_close_form = self.browser.find_element(By.XPATH, '//a[text()="Закрыть форму"]')
        button_close_form.click()

    def check_kvit(self): # Проверка квитированного события в журнале
        IsConfirmed2_Action7 = self.browser.find_elements(By.XPATH, '//td/span/span')
        ConfirmedDate7 = self.browser.find_elements(By.XPATH, '//td/span')
        assert self.check_text(IsConfirmed2_Action7[2], 'Да'), 'Нет данных встолбце IsConfirmed'
        assert self.check_text(IsConfirmed2_Action7[7], 'Квитировано'), 'Нет данных встолбце Action'
        assert self.check_text_not(ConfirmedDate7[7], '-'), 'Нет данных встолбце ConfirmedDate'
    
    def add_comment(self): # Добавление комменария
        button_add_comment = self.browser.find_element(By.CSS_SELECTOR, '[title="Добавить комментарий"]')    
        button_add_comment.click()
        comment_area = self.browser.find_element(By.CSS_SELECTOR, '[ng-model="commentInput.value"]')
        comment_area.clear()
        comment_area.send_keys("Auto test 123 №")
        button_save_comment = self.browser.find_element(By.CSS_SELECTOR, '[class="comments-block__button comments-button comments-button__tick"]')
        button_save_comment.click()
        button_save_form = self.browser.find_element(By.XPATH, '//a[text()="Сохранить"]')
        button_save_form.click()
        button_close_form = self.browser.find_element(By.XPATH, '//a[text()="Закрыть форму"]')
        button_close_form.click()
        field_comment = self.browser.find_elements(By.CSS_SELECTOR, '[role="gridcell"]')
        assert self.check_text(field_comment[12], 'Администратор системы(sam) : Auto test 123 №'), 'Комментарий не виден в журнале'

    def check_comment(self): # Проверка комментария в журнале
        field_comment = self.browser.find_elements(By.CSS_SELECTOR, '[role="gridcell"]')
        assert self.check_text(field_comment[12], 'Администратор системы(sam) : Auto test 123 №'), 'Комментарий не виден в журнале после обновления страницы'  

    def select_recomend(self): # Выбор рекомендаций
        button_recomend = self.browser.find_elements(By.CSS_SELECTOR, '[class="recomendations-tab__arrow-cb arrow-cb"]')
        button_recomend[0].click()
        button_recomend[1].click()
        button_recomend[2].click()
        checkbox_recomend = self.browser.find_elements(By.CSS_SELECTOR, '[class="recomendations-tab__custom-cb custom-cb"]')
        checkbox_recomend[0].click()
        checkbox_recomend[1].click()
        button_save_form = self.browser.find_element(By.XPATH, '//a[text()="Сохранить"]')
        button_save_form.click()
        time.sleep(1)
        assert self.is_element_invisibility(By.CSS_SELECTOR, '[class="popup__save-spinner ng-hide"]'), "Не сохраняется изменения  в Рекомендациях"
        button_close_form = self.browser.find_element(By.XPATH, '//a[text()="Закрыть форму"]')
        button_close_form.click()

    def check_save_recomend(self): # Проверка изменений во вкладке Рекомендация
        check_button_recomend = self.browser.find_elements(By.CSS_SELECTOR, '[class="arrow-cb__input ng-pristine ng-untouched ng-valid ng-not-empty"]')
        assert len(check_button_recomend) == 3, "Выбранно три рекомендации"
        check_checkbox_recomend = self.browser.find_elements(By.CSS_SELECTOR, '[class="custom-cb__input ng-pristine ng-untouched ng-valid ng-not-empty"]')
        assert len(check_checkbox_recomend) == 2, "Выбранно два чекбокса"

    def open_tab_trend(self): # Открытие вкладки Тренд
        button_open_trend = self.browser.find_element(By.CSS_SELECTOR, '[title="Тренд"]')
        button_open_trend.click()
        text_trend = self.browser.find_element(By.XPATH, '//p[text()="Связанные с событием тренды"]')
        assert self.check_text(text_trend, 'Связанные с событием тренды'), "Вкладка Тренд не открылась"        

    def select_trend(self): # Выбор тренда Тренд отклонения вверх
        select_trend_otklon_up = self.browser.find_elements(By.CSS_SELECTOR, '[class="k-icon k-i-arrow-s"]')        
        select_trend_otklon_up[1].click()        
        select = self.browser.find_element(By.XPATH, '//li[text()="Тренд отклонения вверх"]')
        select.click()
        time.sleep(1)      

    #def check_trend(self): # Проверка тренда
        #assert self.is_element_present_with_waiting(By.CSS_SELECTOR, '[class="highcharts-plot-background"]'), 'Нет тренда на графике'

    def open_tab_doc(self): # Открытие вкладки Документы
        button_open_doc = self.browser.find_element(By.CSS_SELECTOR, '[title="Документы"]')
        button_open_doc.click()   
        text_doc = self.browser.find_element(By.XPATH, '//p[text()="Связанные с событием документы"]')
        assert self.check_text(text_doc, 'Связанные с событием документы'), "Вкладка Документы не открылась"
        
    def add_doc(self): # Добавление документа
        button_add_invest = self.browser.find_element(By.CSS_SELECTOR, '[title="Добавить вложение"]')
        button_add_invest.click()
        button_select_file = self.browser.find_elements(By.CSS_SELECTOR, '[type="file"]')
        button_select_file[1].send_keys(self.enter_file('for_auto_test.txt'))
        enter_comment = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="введите комментарий"]')
        enter_comment.clear()
        enter_comment.send_keys("Comment Комментарий №123")
        button_save = self.browser.find_elements(By.CSS_SELECTOR, '.modal-button.pull-right .ui-button-text')
        button_save[0].click()        
        name_doc = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.name"]')
        description_doc = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.description"]')
        assert self.check_text(name_doc[2], 'for_auto_test.txt') and self.check_text(description_doc[2], 'Comment Комментарий №123'), 'Документ не добавился'

    def check_doc(self): # Проверка наличия нового документа после обновления страницы  
        name_doc = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.name"]')
        description_doc = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.description"]')
        assert self.check_text(name_doc[2], 'for_auto_test.txt') and self.check_text(description_doc[2], 'Comment Комментарий №123'), 'Документ не добавился'

    def open_tab_stat(self): # Открытие вкладки Статистика
        button_open_stat = self.browser.find_element(By.CSS_SELECTOR, '[title="Статистика"]')
        button_open_stat.click()   
        text_stat = self.browser.find_element(By.XPATH, '//p[text()="Статистика событий"]')
        assert self.check_text(text_stat, 'Статистика событий'), "Вкладка Статистика не открылась" 

    def filter_for_model_proizvodsva(self): # Фильтрация по модели производства        
        open_model = self.browser.find_element(By.CSS_SELECTOR, '[class="k-icon k-plus"]')
        open_model.click()
        time.sleep(1)
        open_model = self.browser.find_element(By.CSS_SELECTOR, '[class="k-icon k-plus"]')
        open_model.click()
        time.sleep(1)
        model_proizvodsva = self.browser.find_elements(By.CSS_SELECTOR, '[class="k-in ng-binding"]')
        model_proizvodsva[2].click()
        time.sleep(1)
        filter_menu = self.browser.find_element(By.CSS_SELECTOR, '[title="Показать события в таблице"]')
        filter_menu.click()
        number_page = self.browser.find_element(By.CSS_SELECTOR, '[class="k-pager-info k-label"]')
        assert self.is_element_no_text_wating(number_page, number_page.text), 'Колличество событий на странице не изменилось'
        name_model_proizvodsva = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.eventColumn.ObservableObject"]')
        lond_list = len(name_model_proizvodsva)
        assert self.check_list_eq(name_model_proizvodsva, lond_list, 'Белизна, %'), 'Есть события не из Белизна, %'

    def check_rights_PMM(self): # Проверка ограничения прав доступа в PMM
        open_model = self.browser.find_element(By.CSS_SELECTOR, '[class="k-icon k-plus"]')
        open_model.click()
        time.sleep(1)
        open_model = self.browser.find_element(By.CSS_SELECTOR, '[class="k-icon k-plus"]')
        open_model.click()
        time.sleep(1)
        model_proizvodsva = self.browser.find_elements(By.CSS_SELECTOR, '[class="k-in ng-binding"]')
        assert self.check_text(model_proizvodsva[2], 'Гидромодуль в Impbin'), 'Первый элемент в меню не Гидромодуль в Impbin'

    def time_filter(self): # Фильтрация по времени в журнале PMM
        start_date = self.browser.find_element(By.CSS_SELECTOR, '[id="startDatePicker"]')
        start_date.clear()        
        for i in range(16):
            start_date.send_keys(Keys.BACKSPACE)        
        start_date.send_keys("18.04.2021 14:40")
        start_time_filter = self.browser.find_element(By.CSS_SELECTOR, '[title="применить временной диапазон"]')
        start_time_filter.click()
        number_page = self.browser.find_element(By.CSS_SELECTOR, '[class="k-pager-info k-label"]')
        assert self.is_element_no_text_wating(number_page, number_page.text), 'Колличество событий на странице не изменилось'
        
    def change_namder_event(self): # Изменение числа событий на странице
        namber_event_before = self.browser.find_element(By.CSS_SELECTOR, '[class="k-pager-info k-label"]')
        text_namber_event_before = namber_event_before.text        
        list_posible = self.browser.find_element(By.CSS_SELECTOR, '[title="Список возможностей"]')
        list_posible.click()
        settings_menu = self.browser.find_element(By.CSS_SELECTOR, '.settings-menu-link')
        settings_menu.click()
        settings_pmm = self.browser.find_element(By.CSS_SELECTOR, '[title="КТР"]')
        settings_pmm.click()
        change_nmber_event = self.browser.find_element(By.CSS_SELECTOR, '[id="events-count-on-page"]')
        change_nmber_event.clear() 
        change_nmber_event.send_keys("10")                    
        pmm_button = self.browser.find_element(By.XPATH, '//a[text()="KTP"]')
        pmm_button.click()                   
        assert self.is_element_present_with_waiting(By.XPATH, '//span[text()="Неквитированные"]'), "Нет кнопки неквитировано"
        assert self.is_element_present_with_waiting(By.CSS_SELECTOR, '[style="background: rgb(255, 216, 0);"'), "Нет событий в PMM"
        namber_event = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.eventColumn.Action"]')
        namber_event_after = self.browser.find_element(By.CSS_SELECTOR, '[class="k-pager-info k-label"]')
        assert len(namber_event) == 10, "Не совпадает колличество событий на странице"
        assert text_namber_event_before != namber_event_after.text, "Не изменилось количество событий в нижней части журнала"

    def change_namber_event_after_test(self): # Возвращение 20 событий на странице   
        list_posible = self.browser.find_element(By.CSS_SELECTOR, '[title="Список возможностей"]')
        list_posible.click()
        settings_menu = self.browser.find_element(By.CSS_SELECTOR, '.settings-menu-link')
        settings_menu.click()
        settings_pmm = self.browser.find_element(By.CSS_SELECTOR, '[title="КТР"]')
        settings_pmm.click()
        change_nmber_event = self.browser.find_element(By.CSS_SELECTOR, '[id="events-count-on-page"]')
        change_nmber_event.clear() 
        change_nmber_event.send_keys("20") 
        pmm_button = self.browser.find_element(By.XPATH, '//a[text()="KTP"]')
        pmm_button.click()                   
        assert self.is_element_present_with_waiting(By.XPATH, '//span[text()="Неквитированные"]'), "Нет кнопки неквитировано"
        assert self.is_element_present_with_waiting(By.CSS_SELECTOR, '[style="background: rgb(255, 216, 0);"'), "Нет событий в PMM"
        namber_event = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.eventColumn.Action"]')        
        assert len(namber_event) == 20, "Не совпадает колличество событий на странице"




     





    def filter_act_cvit(self): # Фильтрация по "Активны" + "Квитированные"
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]')
        number_filter[0].click()         
        self.is_element_text_wating(number_filter[1], '0') 
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]') 
        active = number_filter[0].text
        no_active = number_filter[1].text
        kvit = number_filter[2].text
        no_kvit = number_filter[3].text       
        assert int(active) == int(kvit) + int(no_kvit), 'Сумма Квит и Неквит не равна Активным'
        status_code = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.eventColumn.StatusCode"]')
        long_list = len(status_code)
        assert self.check_list_no_eq(status_code, long_list, '1'), 'В журнале есть события со статусом 1'
        number_filter[2].click()
        self.is_element_text_wating(number_filter[3], '0')
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]') 
        active = number_filter[0].text
        no_active = number_filter[1].text
        kvit = number_filter[2].text
        no_kvit = number_filter[3].text
        assert int(active) == int(kvit), 'Квит не равна Активным'
        status_code = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.eventColumn.StatusCode"]')
        long_list = len(status_code)
        assert self.check_list_no_eq(status_code, long_list, '1'), 'В журнале есть события со статусом 1'
        IsConfirmed = self.browser.find_elements(By.XPATH, '//td/span/span')
        long_list = len(IsConfirmed)
        assert self.check_list_no_eq_not_0(IsConfirmed, long_list, 'Нет'), 'В журнале есть события со статусом квитирования Нет'


    def filter_act_nocvit(self): # Фильтрация по "Активны" + "Неквитированные"
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]')         
        number_filter[0].click()
        self.is_element_text_wating(number_filter[1], '0') 
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]') 
        active = number_filter[0].text
        no_active = number_filter[1].text
        kvit = number_filter[2].text
        no_kvit = number_filter[3].text       
        assert int(active) == int(kvit) + int(no_kvit), 'Сумма Квит и Неквит не равна Активным'
        status_code = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.eventColumn.StatusCode"]')
        long_list = len(status_code)
        assert self.check_list_no_eq(status_code, long_list, '1'), 'В журнале есть события со статусом 1'
        number_filter[3].click()
        self.is_element_text_wating(number_filter[2], '0')
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]') 
        active = number_filter[0].text
        no_active = number_filter[1].text
        kvit = number_filter[2].text
        no_kvit = number_filter[3].text
        assert int(active) == int(no_kvit), 'Неквит не равна Активным'
        status_code = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.eventColumn.StatusCode"]')
        long_list = len(status_code)
        assert self.check_list_no_eq(status_code, long_list, '1'), 'В журнале есть события со статусом 1'
        IsConfirmed = self.browser.find_elements(By.XPATH, '//td/span/span')
        long_list = len(IsConfirmed)
        assert self.check_list_no_eq_not_0(IsConfirmed, long_list, 'Да'), 'В журнале есть события со статусом квитирования Да'

    def filter_noact_cvit(self): # Фильтрация по "Завершены" + "Квитированные"
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]')         
        number_filter[1].click()
        self.is_element_text_wating(number_filter[0], '0') 
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]') 
        active = number_filter[0].text
        no_active = number_filter[1].text
        kvit = number_filter[2].text
        no_kvit = number_filter[3].text       
        assert int(no_active) == int(kvit) + int(no_kvit), 'Сумма Квит и Неквит не равна Завершены'
        status_code = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.eventColumn.StatusCode"]')
        long_list = len(status_code)
        assert self.check_list_eq(status_code, long_list, '1'), 'В журнале есть события со статусом не 1'
        number_filter[2].click()
        self.is_element_text_wating(number_filter[3], '0')
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]') 
        active = number_filter[0].text
        no_active = number_filter[1].text
        kvit = number_filter[2].text
        no_kvit = number_filter[3].text
        assert int(no_active) == int(kvit), 'Квит не равна Завершены'
        status_code = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.eventColumn.StatusCode"]')
        long_list = len(status_code)
        assert self.check_list_eq(status_code, long_list, '1'), 'В журнале есть события со статусом не 1'
        IsConfirmed = self.browser.find_elements(By.XPATH, '//td/span/span')
        long_list = len(IsConfirmed)
        assert self.check_list_no_eq_not_0(IsConfirmed, long_list, 'Нет'), 'В журнале есть события со статусом квитирования Нет'

    def filter_noact_nocvit(self): # Фильтрация по "Завершены" + "Неквитированные"
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]')         
        number_filter[1].click()
        self.is_element_text_wating(number_filter[0], '0') 
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]') 
        active = number_filter[0].text
        no_active = number_filter[1].text
        kvit = number_filter[2].text
        no_kvit = number_filter[3].text       
        assert int(no_active) == int(kvit) + int(no_kvit), 'Сумма Квит и Неквит не равна Завершены'
        status_code = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.eventColumn.StatusCode"]')
        long_list = len(status_code)
        assert self.check_list_eq(status_code, long_list, '1'), 'В журнале есть события со статусом не 1'
        number_filter[3].click()
        self.is_element_text_wating(number_filter[2], '0')
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]') 
        active = number_filter[0].text
        no_active = number_filter[1].text
        kvit = number_filter[2].text
        no_kvit = number_filter[3].text
        assert int(no_active) == int(no_kvit), 'Неквит не равна Завершены'
        status_code = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.eventColumn.StatusCode"]')
        long_list = len(status_code)
        assert self.check_list_eq(status_code, long_list, '1'), 'В журнале есть события со статусом не 1'
        IsConfirmed = self.browser.find_elements(By.XPATH, '//td/span/span')
        long_list = len(IsConfirmed)
        assert self.check_list_no_eq_not_0(IsConfirmed, long_list, 'Да'), 'В журнале есть события со статусом квитирования Да'   

    def filter_cvit_act(self): # Фильтрация по "Квитированные" + "Активны"
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]')
        number_filter[2].click()         
        self.is_element_text_wating(number_filter[3], '0') 
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]') 
        active = number_filter[0].text
        no_active = number_filter[1].text
        kvit = number_filter[2].text
        no_kvit = number_filter[3].text       
        assert int(kvit) == int(active) + int(no_active), 'Сумма Активные и Завершены не равна Квит'
        IsConfirmed = self.browser.find_elements(By.XPATH, '//td/span/span')
        long_list = len(IsConfirmed)
        assert self.check_list_no_eq_not_0(IsConfirmed, long_list, 'Нет'), 'В журнале есть события со статусом квитирования Нет'
        number_filter[0].click()
        self.is_element_text_wating(number_filter[1], '0')
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]') 
        active = number_filter[0].text
        no_active = number_filter[1].text
        kvit = number_filter[2].text
        no_kvit = number_filter[3].text
        assert int(active) == int(kvit), 'Квит не равна Активным'
        IsConfirmed = self.browser.find_elements(By.XPATH, '//td/span/span')
        long_list = len(IsConfirmed)
        assert self.check_list_no_eq_not_0(IsConfirmed, long_list, 'Нет'), 'В журнале есть события со статусом квитирования Нет'
        status_code = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.eventColumn.StatusCode"]')
        long_list = len(status_code)
        assert self.check_list_no_eq(status_code, long_list, '1'), 'В журнале есть события со статусом 1'

    def filter_cvit_noact(self): # Фильтрация по "Квитированные" + "Завершены"
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]')
        number_filter[2].click()         
        self.is_element_text_wating(number_filter[3], '0') 
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]') 
        active = number_filter[0].text
        no_active = number_filter[1].text
        kvit = number_filter[2].text
        no_kvit = number_filter[3].text       
        assert int(kvit) == int(active) + int(no_active), 'Сумма Активные и Завершены не равна Квит'
        IsConfirmed = self.browser.find_elements(By.XPATH, '//td/span/span')
        long_list = len(IsConfirmed)
        assert self.check_list_no_eq_not_0(IsConfirmed, long_list, 'Нет'), 'В журнале есть события со статусом квитирования Нет'
        number_filter[1].click()
        self.is_element_text_wating(number_filter[0], '0')
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]') 
        active = number_filter[0].text
        no_active = number_filter[1].text
        kvit = number_filter[2].text
        no_kvit = number_filter[3].text
        assert int(no_active) == int(kvit), 'Квит не равна Активным'
        IsConfirmed = self.browser.find_elements(By.XPATH, '//td/span/span')
        long_list = len(IsConfirmed)
        assert self.check_list_no_eq_not_0(IsConfirmed, long_list, 'Нет'), 'В журнале есть события со статусом квитирования Нет'
        status_code = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.eventColumn.StatusCode"]')
        long_list = len(status_code)
        assert self.check_list_eq(status_code, long_list, '1'), 'В журнале есть события со статусом не 1'             

    def filter_nocvit_act(self): # Фильтрация по "Неквитированные" + "Активны"
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]')
        number_filter[3].click()         
        self.is_element_text_wating(number_filter[2], '0') 
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]') 
        active = number_filter[0].text
        no_active = number_filter[1].text
        kvit = number_filter[2].text
        no_kvit = number_filter[3].text       
        assert int(no_kvit) == int(active) + int(no_active), 'Сумма Активные и Завершены не равна Неквит'
        IsConfirmed = self.browser.find_elements(By.XPATH, '//td/span/span')
        long_list = len(IsConfirmed)
        assert self.check_list_no_eq_not_0(IsConfirmed, long_list, 'Да'), 'В журнале есть события со статусом квитирования Нет'
        number_filter[0].click()
        self.is_element_text_wating(number_filter[1], '0')
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]') 
        active = number_filter[0].text
        no_active = number_filter[1].text
        kvit = number_filter[2].text
        no_kvit = number_filter[3].text
        assert int(active) == int(no_kvit), 'Неквит не равна Активным'
        IsConfirmed = self.browser.find_elements(By.XPATH, '//td/span/span')
        long_list = len(IsConfirmed)
        assert self.check_list_no_eq_not_0(IsConfirmed, long_list, 'Да'), 'В журнале есть события со статусом квитирования Нет'
        status_code = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.eventColumn.StatusCode"]')
        long_list = len(status_code)
        assert self.check_list_no_eq(status_code, long_list, '1'), 'В журнале есть события со статусом 1'      

    def filter_nocvit_noact(self): # Фильтрация по "Неквитированные" + "Завершены"
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]')
        number_filter[3].click()         
        self.is_element_text_wating(number_filter[2], '0') 
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]') 
        active = number_filter[0].text
        no_active = number_filter[1].text
        kvit = number_filter[2].text
        no_kvit = number_filter[3].text       
        assert int(no_kvit) == int(active) + int(no_active), 'Сумма Активные и Завершены не равна Квит'
        IsConfirmed = self.browser.find_elements(By.XPATH, '//td/span/span')
        long_list = len(IsConfirmed)
        assert self.check_list_no_eq_not_0(IsConfirmed, long_list, 'Да'), 'В журнале есть события со статусом квитирования Нет'
        number_filter[1].click()
        self.is_element_text_wating(number_filter[0], '0')
        number_filter = self.browser.find_elements(By.CSS_SELECTOR, '[class="summary-item-number ng-binding"]') 
        active = number_filter[0].text
        no_active = number_filter[1].text
        kvit = number_filter[2].text
        no_kvit = number_filter[3].text
        assert int(no_active) == int(no_kvit), 'Неквит не равна Активным'
        IsConfirmed = self.browser.find_elements(By.XPATH, '//td/span/span')
        long_list = len(IsConfirmed)
        assert self.check_list_no_eq_not_0(IsConfirmed, long_list, 'Да'), 'В журнале есть события со статусом квитирования Нет'
        status_code = self.browser.find_elements(By.CSS_SELECTOR, '[ng-bind="dataItem.eventColumn.StatusCode"]')
        long_list = len(status_code)
        assert self.check_list_eq(status_code, long_list, '1'), 'В журнале есть события со статусом не 1'


    

            




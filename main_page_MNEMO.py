from attr import s
from pip._vendor import requests
from selenium.webdriver.common import by
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class MainPageMNEMO(BasePage):
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
        assert self.is_element_present(By.XPATH, '//a[text()="АВТОТЕСТЫ"]'), "Не авторизовался" 

    def check_limit_rights_on_start_page(self): # Проверка ограничений прав на главной странице
        assert self.is_element_no_present(By.XPATH, '//a[text()="Bugs"]'), "Не работают ограничения прав доступа на главной странице"

    def open_mnemo(self): # Открытие мнемосхемы с value   
        button_autotest = self.browser.find_element(By.XPATH, '//a[text()="АВТОТЕСТЫ"]')
        button_autotest.click()
        button_values = self.browser.find_element(By.XPATH, '//a[text()="Values"]')
        button_values.click()
        lable_smarttrend = self.browser.find_element(By.CSS_SELECTOR, '[class="st4f9529426-8e32-4df8-aefe-201119884d38"]')
        assert self.check_text(lable_smarttrend, 'SmartTrend'), 'Нет SmartTrend'

    def open_mnemo_zonemaker(self): # Открытие мнемосхемы с ZoneMakers
        button_autotest = self.browser.find_element(By.XPATH, '//a[text()="АВТОТЕСТЫ"]')
        button_autotest.click()
        button_values = self.browser.find_element(By.XPATH, '//a[text()="ZoneMaker"]')
        button_values.click()
        assert self.is_element_present(By.CSS_SELECTOR, '[class="st34f2119a4-a0d6-4d5b-9a3d-f34cdd6f3383"]'), "Не открылась мнемосхема с ZoneMakers"    

    def check_value_load(self): # Проверка загрузки значений value
        value_check = self.browser.find_elements(By.CSS_SELECTOR, '[class="st11baa52155-2fa0-4d3a-b470-7490a692c382"]')
        assert self.is_element_no_text_wating(value_check[10], '-'), 'Значения не загрузились'

    def check_value(self): # Проверка значений value    
        value_pi = ['123', '123.46', '123.457', '123.457', '123.4568', '123.457', '123.4568', '123.4568 kg', 'kg', '12313:07:14']
        value_af = ['123', '123.46', '123.457', '123.457', '123.45678', '123.45678', '123.45678', '123.45678 kg', '12303:00:00', 'kg']
        value_historian = ['62.6', '62.60', '62.600', '62.600', '62.6', '62.6', '62.6', '62.6 kg', 'kg', '6316:32:20']
        value = self.browser.find_elements(By.CSS_SELECTOR, '[class="st11baa52155-2fa0-4d3a-b470-7490a692c382"]')                           
        assert self.check_list_value(value, 0, value_pi), "Не совпадают значения Pi"
        assert self.check_list_value(value, 10, value_af), "Не совпадают значения Af" 
        assert self.check_list_value(value, 20, value_historian), "Не совпадают значения Historian"


    def check_smart_trend(self): # Проверка Smart Trend        
        button_select_param = self.browser.find_elements(By.XPATH, '//span[text()="Выбор параметров"]') 
        button_select_param[0].click() 
        value_pi = self.browser.find_element(By.CSS_SELECTOR, '[data-targetid="37fd8465-e462-4af2-b269-d95b0262b80b"]')
        value_pi.click()
        button_select = self.browser.find_element(By.CSS_SELECTOR, '[class="select2-selection select2-selection--single"')
        button_select.click()
        button_select_smarttrend = self.browser.find_element(By.XPATH, '//span[text()="SmartTrandMaxi"]')
        button_select_smarttrend.click()        
        button_unload_select = self.browser.find_element(By.CSS_SELECTOR, '[class="header-button icon-button trend-parameters-send"]')
        button_unload_select.click()
        assert self.is_element_present(By.CSS_SELECTOR, '[class="highcharts-series highcharts-series-0 highcharts-line-series highcharts-color-undefined "]'), 'Нет графика на SmartTrend'
        bytton_plise_size = self.browser.find_element(By.CSS_SELECTOR, '[title="Увеличить"]')
        bytton_plise_size.click()
        bytton_plise_size.click()
        bytton_plise_size.click()
        bytton_plise_size.click()
        time.sleep(1)
        assert self.is_element_present(By.CSS_SELECTOR, '[class="highcharts-legend-box"]'), "Нет легенды на SmartTrend"
        trend_info = self.browser.find_elements(By.CSS_SELECTOR, '[transform="translate(0,0)"]')        
        assert self.check_text(trend_info[2], 'PI.\\\DEVELOP_PMM2\Static tag for autotests kg'), "Нет информации о тренде"

    def full_screan_smart_trend(self): # Открытие Smart Trend на полный экран        
        smart_trend = self.browser.find_element(By.CSS_SELECTOR, '[class="highcharts-background"]')
        self.double_click(smart_trend)        
        assert self.is_element_present(By.CSS_SELECTOR, '[title="Установить курсор"]') and self.is_element_present(By.CSS_SELECTOR, '[title="Удалить всё курсоры"]'), "SmartTrend не открылся на весь через дабл клик"
        assert self.is_element_present(By.CSS_SELECTOR, '[class="highcharts-series highcharts-series-0 highcharts-line-series highcharts-color-undefined "]'), 'Нет графика на SmartTrend'
        assert self.is_element_present(By.CSS_SELECTOR, '[class="highcharts-legend-box"]'), "Нет легенды на SmartTrend"
        button_no_full_screan = self.browser.find_element(By.CSS_SELECTOR, '[title="Восстановить размер"]')
        button_no_full_screan.click()
        time.sleep(1)
        buttom_menu = self.browser.find_element(By.CSS_SELECTOR, '[class="sm-tr-btn-list"]')
        buttom_menu.click()
        button_full_screan = self.browser.find_element(By.CSS_SELECTOR, '[title="Во весь экран"]')
        button_full_screan.click()
        assert self.is_element_present(By.CSS_SELECTOR, '[title="Установить курсор"]') and self.is_element_present(By.CSS_SELECTOR, '[title="Удалить всё курсоры"]'), "SmartTrend не открылся на весь через кнопку"
        assert self.is_element_present(By.CSS_SELECTOR, '[class="highcharts-series highcharts-series-0 highcharts-line-series highcharts-color-undefined "]'), 'Нет графика на SmartTrend'
        assert self.is_element_present(By.CSS_SELECTOR, '[class="highcharts-legend-box"]'), "Нет легенды на SmartTrend"

    def check_new_graph(self): # Проверка Новый график
        button_select_param = self.browser.find_elements(By.XPATH, '//span[text()="Выбор параметров"]') 
        button_select_param[0].click() 
        value_pi = self.browser.find_element(By.CSS_SELECTOR, '[data-targetid="37fd8465-e462-4af2-b269-d95b0262b80b"]')
        value_pi.click()
        button_select = self.browser.find_element(By.CSS_SELECTOR, '[class="select2-selection select2-selection--single"')
        button_select.click()
        button_select_new_graf = self.browser.find_element(By.XPATH, '//span[text()="Новый график"]')
        button_select_new_graf.click()        
        button_unload_select = self.browser.find_element(By.CSS_SELECTOR, '[class="header-button icon-button trend-parameters-send"]')
        button_unload_select.click()
        button_unload_select_new_window = self.browser.find_element(By.CSS_SELECTOR, '[class="header-button icon-button trend-parameters-send-to-child-window"]')
        button_unload_select_new_window.click()
        time.sleep(1)
        new_tab = self.browser.window_handles[1]
        self.browser.switch_to.window(new_tab)        
        assert self.is_element_present(By.CSS_SELECTOR, '[class="highcharts-series-group"]'), 'Нет графика на тренде'
        assert self.is_element_present(By.CSS_SELECTOR, '[class="highcharts-legend-box"]'), "Нет легенды на тренде"
        assert self.browser.find_element(By.CSS_SELECTOR, '[title="Статичный тэг для автотестов"]').text == 'Статичный тэг для автотестов', "Нет названия тега"
        assert self.browser.find_element(By.CSS_SELECTOR, '[title=" kg"]').text == 'kg', "Нет единиц измерения"
        new_window = self.browser.window_handles[2]
        self.browser.switch_to.window(new_window)        
        assert self.is_element_present(By.CSS_SELECTOR, '[class="highcharts-series-group"]'), 'Нет графика на тренде'
        assert self.is_element_present(By.CSS_SELECTOR, '[class="highcharts-legend-box"]'), "Нет легенды на тренде"
        assert self.browser.find_element(By.CSS_SELECTOR, '[title="Статичный тэг для автотестов"]').text == 'Статичный тэг для автотестов', "Нет названия тега"
        assert self.browser.find_element(By.CSS_SELECTOR, '[title=" kg"]').text == 'kg', "Нет единиц измерения" 
        
    def simple_trend(self): # Проверка Простой тренд    
        value = self.browser.find_elements(By.CSS_SELECTOR, '[class="st11baa52155-2fa0-4d3a-b470-7490a692c382"]')
        value[1].click()
        button_trend = self.browser.find_element(By.XPATH, '//div[text()="Тренд"]')
        button_trend.click()
        assert self.is_element_present(By.CSS_SELECTOR, '[class="highcharts-tracker"]'), 'Нет графика на тренде'
        assert self.is_element_present(By.XPATH, '//span[text()="Печать"]'), 'Нет кнопки Печать'
        assert self.is_element_present(By.XPATH, '//span[text()=">"]'), 'Нет кнопки >'
        assert self.is_element_present(By.XPATH, '//span[text()="<"]'), 'Нет кнопки <'
        assert self.is_element_present(By.XPATH, '//span[text()="Сброс"]'), 'Нет кнопки Сброс'
        button_close = self.browser.find_element(By.CSS_SELECTOR, '[title="Close"]')
        button_close.click()
        value[11].click()
        button_trend = self.browser.find_element(By.XPATH, '//div[text()="Тренд"]')
        button_trend.click()
        assert self.is_element_present(By.CSS_SELECTOR, '[class="highcharts-tracker"]'), 'Нет графика на тренде'
        assert self.is_element_present(By.XPATH, '//span[text()="Печать"]'), 'Нет кнопки Печать'
        assert self.is_element_present(By.XPATH, '//span[text()=">"]'), 'Нет кнопки >'
        assert self.is_element_present(By.XPATH, '//span[text()="<"]'), 'Нет кнопки <'
        assert self.is_element_present(By.XPATH, '//span[text()="Сброс"]'), 'Нет кнопки Сброс'
        button_close = self.browser.find_element(By.CSS_SELECTOR, '[title="Close"]')
        button_close.click()
        value[21].click()
        button_trend = self.browser.find_element(By.XPATH, '//div[text()="Тренд"]')
        button_trend.click()
        assert self.is_element_present(By.CSS_SELECTOR, '[class="highcharts-tracker"]'), 'Нет графика на тренде'
        assert self.is_element_present(By.XPATH, '//span[text()="Печать"]'), 'Нет кнопки Печать'
        assert self.is_element_present(By.XPATH, '//span[text()=">"]'), 'Нет кнопки >'
        assert self.is_element_present(By.XPATH, '//span[text()="<"]'), 'Нет кнопки <'
        assert self.is_element_present(By.XPATH, '//span[text()="Сброс"]'), 'Нет кнопки Сброс'
        button_close = self.browser.find_element(By.CSS_SELECTOR, '[title="Close"]')
        button_close.click()

    def check_bar(self): # Проверка Баров
        value_bar = self.browser.find_elements(By.CSS_SELECTOR, '[class="st14c4ea2918-4f0e-4003-85ab-0a0e977ec2fc"]')
        assert self.check_text(value_bar[0], '111'), "Нет данных в баре PI"
        assert self.check_text(value_bar[1], '123'), "Нет данных в баре AF"
        #assert self.check_text(value_bar[2], '62'), "Нет данных в баре Historian"
        assert self.is_element_present(By.CSS_SELECTOR, '[height="78.60076560974122"]'), 'Нет столбца на баре PI'
        assert self.is_element_present(By.CSS_SELECTOR, '[height="116.56213126382445"]'), 'Нет столбца на баре AF'

    def table_from_select_param(self): # Выгрузка в таблицу через Выбор параметров 
        button_select_param = self.browser.find_elements(By.XPATH, '//span[text()="Выбор параметров"]') 
        button_select_param[0].click() 
        value_pi = self.browser.find_element(By.CSS_SELECTOR, '[data-targetid="37fd8465-e462-4af2-b269-d95b0262b80b"]')
        value_pi.click()
        button_select = self.browser.find_element(By.CSS_SELECTOR, '[class="select2-selection select2-selection--single"')
        button_select.click()
        button_select_table = self.browser.find_element(By.XPATH, '//span[text()="Вывести данные в таблицу"]')
        button_select_table.click()        
        button_unload_select = self.browser.find_element(By.CSS_SELECTOR, '[class="header-button icon-button trend-parameters-send"]')
        button_unload_select.click()
        button_calendar = self.browser.find_elements(By.CSS_SELECTOR, '[class="ui-datepicker-trigger"]')
        button_calendar[0].click()
        day_twenty = self.browser.find_element(By.XPATH, '//a[text()="1"]')
        day_twenty.click()
        button_calendar[1].click()
        day_twenty_one = self.browser.find_element(By.XPATH, '//a[text()="2"]')
        day_twenty_one.click()
        step = Select(self.browser.find_element(By.CSS_SELECTOR, '[ng-options="item.value as item.name for item in steps"]'))        
        step.select_by_visible_text('1 час')
        button_table = self.browser.find_element(By.XPATH, '//span[text()="Таблица"]')
        button_table.click()
        table = self.browser.find_elements(By.CSS_SELECTOR, '[role="gridcell"]')        
        assert self.check_list_eq_through_one_not_0(table, len(table), '123.46'), "Значения в таблице не совпадают при вышрузке из Выбор параметров"
        buttons_close = self.browser.find_elements(By.XPATH, '//span[text()="Закрыть"]')
        buttons_close[1].click()
        buttons_close[0].click()

    def table_from_smart_trend(self): # Выгрузка в таблицу через SmartTrend
        button_select = self.browser.find_element(By.CSS_SELECTOR, '[class="select2-selection select2-selection--single"')
        button_select.click()
        button_select_smart_trend = self.browser.find_element(By.XPATH, '//span[text()="SmartTrandMaxi"]')
        button_select_smart_trend.click()        
        button_unload_select = self.browser.find_element(By.CSS_SELECTOR, '[class="header-button icon-button trend-parameters-send"]')
        button_unload_select.click()
        buttom_menu = self.browser.find_element(By.CSS_SELECTOR, '[class="sm-tr-btn-list"]')
        buttom_menu.click()
        button_table = self.browser.find_element(By.CSS_SELECTOR, '[title="Вывести данные в таблицу"]')
        button_table.click()
        button_calendar = self.browser.find_elements(By.CSS_SELECTOR, '[class="ui-datepicker-trigger"]')
        button_calendar[0].click()
        day_twenty = self.browser.find_element(By.XPATH, '//a[text()="1"]')
        day_twenty.click()
        button_calendar[1].click()
        day_twenty_one = self.browser.find_element(By.XPATH, '//a[text()="2"]')
        day_twenty_one.click()
        step = Select(self.browser.find_element(By.CSS_SELECTOR, '[ng-options="item.value as item.name for item in steps"]'))        
        step.select_by_visible_text('1 час')
        button_table = self.browser.find_element(By.XPATH, '//span[text()="Таблица"]')
        button_table.click()
        table = self.browser.find_elements(By.CSS_SELECTOR, '[role="gridcell"]')        
        assert self.check_list_eq_through_one_not_0(table, len(table), '123.46'), "Значения в таблице не совпадают при вышрузке из Выбор параметров"
        buttons_close = self.browser.find_elements(By.XPATH, '//span[text()="Закрыть"]')
        buttons_close[1].click()
        buttons_close[0].click()

    def table_from_new_graf(self): # Выгрузка в таблицу через Новый график
        button_select = self.browser.find_element(By.CSS_SELECTOR, '[class="select2-selection select2-selection--single"')
        button_select.click()
        button_select_new_graf = self.browser.find_element(By.XPATH, '//span[text()="Новый график"]')
        button_select_new_graf.click()    
        value_pi = self.browser.find_element(By.CSS_SELECTOR, '[data-targetid="37fd8465-e462-4af2-b269-d95b0262b80b"]')
        value_pi.click()        
        button_unload_select = self.browser.find_element(By.CSS_SELECTOR, '[class="header-button icon-button trend-parameters-send"]')
        button_unload_select.click()        
        time.sleep(1)
        new_tab = self.browser.window_handles[1]
        self.browser.switch_to.window(new_tab)
        buttom_menu = self.browser.find_element(By.CSS_SELECTOR, '[class="sm-tr-btn-list"]')
        buttom_menu.click()
        button_table = self.browser.find_element(By.CSS_SELECTOR, '[title="Вывести данные в таблицу"]')
        button_table.click()
        button_calendar = self.browser.find_elements(By.CSS_SELECTOR, '[class="ui-datepicker-trigger"]')
        button_calendar[0].click()
        day_twenty = self.browser.find_element(By.XPATH, '//a[text()="1"]')
        day_twenty.click()
        button_calendar[1].click()
        day_twenty_one = self.browser.find_element(By.XPATH, '//a[text()="2"]')
        day_twenty_one.click()
        step = Select(self.browser.find_element(By.CSS_SELECTOR, '[ng-options="item.value as item.name for item in steps"]'))        
        step.select_by_visible_text('1 час')
        button_table = self.browser.find_element(By.XPATH, '//span[text()="Таблица"]')
        button_table.click()
        table = self.browser.find_elements(By.CSS_SELECTOR, '[role="gridcell"]')        
        assert self.check_list_eq_through_one_not_0(table, len(table), '123.46'), "Значения в таблице не совпадают при вышрузке из Выбор параметров"
        buttons_close = self.browser.find_elements(By.XPATH, '//span[text()="Закрыть"]')
        buttons_close[1].click()
        buttons_close[0].click()

    def check_zone_maker_setings_visio(self): # Проверка работы ZoneMaker с настройками Visio
        zone_maker_child_window = self.browser.find_elements(By.CSS_SELECTOR, '[class="st16f526610-12b9-4e93-ba93-c15441f67c4a"]')  
        self.move_cursor(zone_maker_child_window[1])
        select_zone_maker = self.browser.find_element(By.CSS_SELECTOR, '[style="cursor: pointer; fill: rgb(255, 0, 0);"]')
        assert self.is_element_present(By.XPATH, '//div[text()="В дочернем окне"]'), "Нет подсказки"
        select_zone_maker.click()
        time.sleep(1)
        old_tab = self.browser.window_handles[0]
        new_tab = self.browser.window_handles[1]
        self.browser.switch_to.window(new_tab)
        lable_smarttrend = self.browser.find_element(By.CSS_SELECTOR, '[class="st4f9529426-8e32-4df8-aefe-201119884d38"]')
        assert self.check_text(lable_smarttrend, 'SmartTrend'), 'Нет SmartTrend'
        self.browser.close()
        self.browser.switch_to.window(old_tab)
        self.move_cursor(zone_maker_child_window[2])
        select_zone_maker = self.browser.find_element(By.CSS_SELECTOR, '[style="cursor: pointer; fill: rgb(255, 0, 0);"]')
        assert self.is_element_present(By.XPATH, '//div[text()="В новой вкладке"]'), "Нет подсказки"
        select_zone_maker.click()
        time.sleep(1)
        old_tab = self.browser.window_handles[0]
        new_tab = self.browser.window_handles[1]
        self.browser.switch_to.window(new_tab)
        lable_smarttrend = self.browser.find_element(By.CSS_SELECTOR, '[class="st4f9529426-8e32-4df8-aefe-201119884d38"]')
        assert self.check_text(lable_smarttrend, 'SmartTrend'), 'Нет SmartTrend'
        self.browser.close()
        self.browser.switch_to.window(old_tab)
        self.move_cursor(zone_maker_child_window[3])
        select_zone_maker = self.browser.find_element(By.CSS_SELECTOR, '[style="cursor: pointer; fill: rgb(255, 0, 0);"]')
        assert self.is_element_present(By.XPATH, '//div[text()="Не открывать (только подсказка)"]'), "Нет подсказки"        
        
    def check_zone_maker_setings_portal(self): # Проверка работы ZoneMaker с настройками Портала
        zone_maker_child_window = self.browser.find_elements(By.CSS_SELECTOR, '[class="st16f526610-12b9-4e93-ba93-c15441f67c4a"]')  
        self.move_cursor(zone_maker_child_window[0])
        select_zone_maker = self.browser.find_element(By.CSS_SELECTOR, '[style="cursor: pointer; fill: rgb(255, 0, 0);"]')
        assert self.is_element_present(By.XPATH, '//div[text()="Настройки портала"]'), "Нет подсказки"
        select_zone_maker.click()
        time.sleep(1)
        lable_smarttrend = self.browser.find_element(By.CSS_SELECTOR, '[class="st4f9529426-8e32-4df8-aefe-201119884d38"]')
        assert self.check_text(lable_smarttrend, 'SmartTrend'), 'Нет SmartTrend'
        list_posible = self.browser.find_element(By.CSS_SELECTOR, '[title="Список возможностей"]')
        list_posible.click()
        settings_menu = self.browser.find_element(By.CSS_SELECTOR, '.settings-menu-link')
        settings_menu.click()
        settings_pmm = self.browser.find_element(By.CSS_SELECTOR, '[title="Мнемосхемы"]')
        settings_pmm.click()
        settinds_zone_maker_open_new_window = self.browser.find_element(By.XPATH, '//div[text()="Открывать ссылки в новом окне"]')
        settinds_zone_maker_open_new_window.click()
        toast_massege = self.browser.find_element(By.CSS_SELECTOR, '[class="toast-message"]')
        assert self.check_text(toast_massege, 'Настройки успешно сохранены.'), "Настройки не сохранились"        
        self.open_mnemo_zonemaker()
        zone_maker_child_window = self.browser.find_elements(By.CSS_SELECTOR, '[class="st16f526610-12b9-4e93-ba93-c15441f67c4a"]')
        self.move_cursor(zone_maker_child_window[0])
        select_zone_maker = self.browser.find_element(By.CSS_SELECTOR, '[style="cursor: pointer; fill: rgb(255, 0, 0);"]') 
        select_zone_maker.click()       
        time.sleep(1)
        old_tab = self.browser.window_handles[0]
        new_tab = self.browser.window_handles[1]
        self.browser.switch_to.window(new_tab)
        lable_smarttrend = self.browser.find_element(By.CSS_SELECTOR, '[class="st4f9529426-8e32-4df8-aefe-201119884d38"]')
        assert self.check_text(lable_smarttrend, 'SmartTrend'), 'Нет SmartTrend'
        self.browser.close()
        self.browser.switch_to.window(old_tab)
        list_posible = self.browser.find_element(By.CSS_SELECTOR, '[title="Список возможностей"]')
        list_posible.click()
        settings_menu = self.browser.find_element(By.CSS_SELECTOR, '.settings-menu-link')
        settings_menu.click()
        settings_pmm = self.browser.find_element(By.CSS_SELECTOR, '[title="Мнемосхемы"]')
        settings_pmm.click()
        settinds_zone_maker_open_new_tab = self.browser.find_element(By.XPATH, '//div[text()="Открывать ссылки в новой вкладке"]')
        settinds_zone_maker_open_new_tab.click()
        toast_massege = self.browser.find_element(By.CSS_SELECTOR, '[class="toast-message"]')
        assert self.check_text(toast_massege, 'Настройки успешно сохранены.'), "Настройки не сохранились"
        self.open_mnemo_zonemaker()
        zone_maker_child_window = self.browser.find_elements(By.CSS_SELECTOR, '[class="st16f526610-12b9-4e93-ba93-c15441f67c4a"]')
        self.move_cursor(zone_maker_child_window[0])
        select_zone_maker = self.browser.find_element(By.CSS_SELECTOR, '[style="cursor: pointer; fill: rgb(255, 0, 0);"]')
        select_zone_maker.click()
        time.sleep(1)
        old_tab = self.browser.window_handles[0]
        new_tab = self.browser.window_handles[1]
        self.browser.switch_to.window(new_tab)
        lable_smarttrend = self.browser.find_element(By.CSS_SELECTOR, '[class="st4f9529426-8e32-4df8-aefe-201119884d38"]')
        assert self.check_text(lable_smarttrend, 'SmartTrend'), 'Нет SmartTrend'
        self.browser.close()
        self.browser.switch_to.window(old_tab)
        list_posible = self.browser.find_element(By.CSS_SELECTOR, '[title="Список возможностей"]')
        list_posible.click()
        settings_menu = self.browser.find_element(By.CSS_SELECTOR, '.settings-menu-link')
        settings_menu.click()
        settings_pmm = self.browser.find_element(By.CSS_SELECTOR, '[title="Мнемосхемы"]')
        settings_pmm.click()
        settinds_zone_maker_open_new_tab = self.browser.find_element(By.XPATH, '//div[text()="Не открывать ссылки. Показывать подсказку"]')
        settinds_zone_maker_open_new_tab.click()
        toast_massege = self.browser.find_element(By.CSS_SELECTOR, '[class="toast-message"]')
        assert self.check_text(toast_massege, 'Настройки успешно сохранены.'), "Настройки не сохранились"
        self.open_mnemo_zonemaker()
        zone_maker_child_window = self.browser.find_elements(By.CSS_SELECTOR, '[class="st16f526610-12b9-4e93-ba93-c15441f67c4a"]')
        self.move_cursor(zone_maker_child_window[0])
        select_zone_maker = self.browser.find_element(By.CSS_SELECTOR, '[style="cursor: pointer; fill: rgb(255, 0, 0);"]')
        assert self.is_element_present(By.XPATH, '//div[text()="Настройки портала"]'), "Нет подсказки"
        select_zone_maker.click()
        time.sleep(1)
        list_posible = self.browser.find_element(By.CSS_SELECTOR, '[title="Список возможностей"]')
        list_posible.click()
        settings_menu = self.browser.find_element(By.CSS_SELECTOR, '.settings-menu-link')
        settings_menu.click()
        settings_pmm = self.browser.find_element(By.CSS_SELECTOR, '[title="Мнемосхемы"]')
        settings_pmm.click()
        settinds_zone_maker_open_new_tab = self.browser.find_element(By.XPATH, '//div[text()="Открывать ссылки в текущей области"]')
        settinds_zone_maker_open_new_tab.click()
        toast_massege = self.browser.find_element(By.CSS_SELECTOR, '[class="toast-message"]')
        assert self.check_text(toast_massege, 'Настройки успешно сохранены.'), "Настройки не сохранились"
        





          


        
        













        





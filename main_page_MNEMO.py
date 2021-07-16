from attr import s
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
        lable_smarttrend = self.browser.find_element(By.CSS_SELECTOR, '[class="st3b2c843f0-44e6-4e4a-a2b6-36382c729b37"]')
        assert self.check_text(lable_smarttrend, 'SmartTrend'), 'Нет SmartTrend'

    def check_value_load(self): # Проверка загрузки значений value
        value_check = self.browser.find_elements(By.CSS_SELECTOR, '[class="st10d2df5849-cf0c-4e14-9754-f1471777592f"]')
        assert self.is_element_no_text_wating(value_check[10], '-'), 'Значения не загрузились'

    def check_value(self): # Проверка значений value    
        value_pi = ['123', '123.46', '123.457', '123.457', '123.4568', '123.457', '123.4568', '123.4568 kg', 'kg', '12313:07:14']
        value = self.browser.find_elements(By.CSS_SELECTOR, '[class="st10d2df5849-cf0c-4e14-9754-f1471777592f"]')                           
        assert self.check_list_value(value, 10, value_pi), "Не совпадают значения Pi" 

    def check_smart_trend(self): # Проверка Smart Trend        
        button_select_param = self.browser.find_elements(By.XPATH, '//span[text()="Выбор параметров"]') 
        button_select_param[0].click() 
        value_pi = self.browser.find_element(By.CSS_SELECTOR, '[data-targetid="0d4d02a7-20dc-418a-8478-6623734a74b0"]')
        value_pi.click()
        button_select = self.browser.find_element(By.CSS_SELECTOR, '[class="select2-selection select2-selection--single"]')
        button_select.click()
        select_SmartTrendMaxi = self.browser.find_elements(By.CSS_SELECTOR, '[role="treeitem"]')
        select_SmartTrendMaxi[1].click()
        button_unload_select = self.browser.find_element(By.CSS_SELECTOR, '[class="header-button icon-button trend-parameters-send"]')
        button_unload_select.click()
        assert self.is_element_present(By.CSS_SELECTOR, '[class="highcharts-series highcharts-series-0 highcharts-line-series highcharts-color-undefined "]'), 'Нет графика на SmartTrend'
        bytton_plise_size = self.browser.find_element(By.CSS_SELECTOR, '[title="Увеличить"]')
        bytton_plise_size.click()
        bytton_plise_size.click()
        assert self.is_element_present(By.CSS_SELECTOR, '[class="highcharts-legend-box"]'), "Нет легенды на SmartTrend"

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
        value_pi = self.browser.find_element(By.CSS_SELECTOR, '[data-targetid="0d4d02a7-20dc-418a-8478-6623734a74b0"]')
        value_pi.click()
        button_select = self.browser.find_element(By.CSS_SELECTOR, '[class="select2-selection select2-selection--single"]')
        button_select.click()
        select_new_graph = self.browser.find_elements(By.CSS_SELECTOR, '[role="treeitem"]')
        select_new_graph[2].click()
        button_unload_select = self.browser.find_element(By.CSS_SELECTOR, '[class="header-button icon-button trend-parameters-send"]')
        button_unload_select.click()
        time.sleep(1)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)        
        assert self.is_element_present(By.CSS_SELECTOR, '[class="highcharts-series-group"]'), 'Нет графика на тренде'
        assert self.is_element_present(By.CSS_SELECTOR, '[class="highcharts-legend-box"]'), "Нет легенды на тренде"


        




    
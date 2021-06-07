from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        tl_button = self.browser.find_element(By.XPATH, '//a[text()="KTP"]')
        tl_button.click()

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
        assert self.is_element_present(By.CSS_SELECTOR, '[ng-click="updateEvent(eventIds)"]') and self.is_element_present(By.XPATH, '//span[text()="Значение пробития границы: "]'), "Карточка события не открывается"

    def press_button_kvit(self): # Нажать на кнопку Квитировать
        button_kvit = self.browser.find_element(By.CSS_SELECTOR, '[ng-click="updateEvent(eventIds)"]')
        button_kvit.click()
        assert self.is_element_present_with_waiting(By.CSS_SELECTOR, '[class="popup__button js-confirm-btn ng-binding popup__top-info-button-disable"]'), 'Кнопка Квитировать активна'
        button_close_form = self.browser.find_element(By.XPATH, '//a[text()="Закрыть форму"]')
        button_close_form.click()

    def check_kvit(self): # Проверка квитированного события в журнале
        fnrnnnn

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

    

            




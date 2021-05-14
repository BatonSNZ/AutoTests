from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class MainPage(BasePage):
    def in_to_login(self): #Авторизация
        username_fild = self.browser.find_element(By.ID, 'txtUserName')
        username_fild.clear()
        username_fild.send_keys("sam")
        password_fild = self.browser.find_element(By.ID, 'txtPassword')
        password_fild.clear()
        password_fild.send_keys("sam")
        enter_button = self.browser.find_element(By.CLASS_NAME, 'btn-login')
        enter_button.click()

    def should_be_start_page(self): #Проверка аторизации
        assert self.is_element_present(By.XPATH, '//a[text()="TL"]'), "Не авторизовался"    

    def open_tl(self): #Открытие TL
        username_fild = self.browser.find_element(By.ID, 'txtUserName')
        username_fild.clear()
        username_fild.send_keys("sam")
        password_fild = self.browser.find_element(By.ID, 'txtPassword')
        password_fild.clear()
        password_fild.send_keys("sam")
        enter_button = self.browser.find_element(By.CLASS_NAME, 'btn-login')
        enter_button.click()
        tl_button = self.browser.find_element(By.XPATH, '//a[text()="TL"]')
        tl_button.click()

    def check_open_tl(self): #Проверка открытия TL
        assert self.is_element_present(By.CSS_SELECTOR, '[class="info-cell-first-column"]'), "TL не открылся"

    def new_event_in_tl_from_button(self): #Создание события Шаблон Шаблоныч через кнопку создать событие
        create_event_button = self.browser.find_element(By.ID, 'addEventBtnId')
        create_event_button.click()
        shablon_event_button = self.browser.find_element(By.ID, '019fa8f1-3475-48b6-bc76-cd05fb357f2f')
        shablon_event_button.click()
        assert self.is_element_present(By.CSS_SELECTOR,'[value="ВЫБРАТЬ..."]'), "Карточка события не открылась или там ошибка"
        work_center_selection_button = self.browser.find_element(By.CSS_SELECTOR, '[value="ВЫБРАТЬ..."]')
        work_center_selection_button.click()
        open_group_ilim = self.browser.find_element(By.CSS_SELECTOR, '.modalWindow.ktp-wrapper.checkbox-wrap .ng-isolate-scope .ng-scope .atp-block .atp-content .atp-content-wrap #atp-panelbar .k-state-active.k-item.k-first.k-last.k-state-highlight .atp-treelist-wrap.k-content .atp-main-list.pmm-custom-scroll .ng-scope.ng-isolate-scope #atp-treelist .k-group.k-treeview-lines .k-item.k-first.k-last .ng-scope.k-top.k-bot .k-icon.k-i-expand')
        open_group_ilim.click()
        open_bratsk = self.browser.find_element(By.CSS_SELECTOR, '.ng-scope.k-last .k-bot .k-icon.k-i-expand')
        open_bratsk.click()
        time.sleep(1)
        open_vspom_struktur_podrasdel = self.browser.find_element(By.CSS_SELECTOR, '.k-item.ng-scope .k-top .k-icon.k-i-expand')
        open_vspom_struktur_podrasdel.click()
        time.sleep(1)
        open_prvo_po_vodopod_i_ing_kommunic = self.browser.find_element(By.CSS_SELECTOR, '.k-group .k-item.ng-scope .k-top .k-icon.k-i-expand')
        open_prvo_po_vodopod_i_ing_kommunic.click()
        time.sleep(1)
        open_seh_ochis_sooruzh_promstokov = self.browser.find_element(By.CSS_SELECTOR, '.k-item.ng-scope.k-last .k-bot .k-icon.k-i-expand')
        open_seh_ochis_sooruzh_promstokov.click()
        time.sleep(1)
        checkbox_ilovai_stantsia_1 = self.browser.find_elements(By.CSS_SELECTOR, '.k-mid .k-in .tl-item-dialog-table .item-selector-lable span')
        checkbox_ilovai_stantsia_1[2].click()
        time.sleep(1)
        enter_edindtsi_oborudovania_button = self.browser.find_element(By.XPATH, '//span[text()="ВЫБРАТЬ"]')
        enter_edindtsi_oborudovania_button.click()
        naimenovanie_rabochego_sentra = self.browser.find_element(By.CSS_SELECTOR, '.standart-input-styles.to-validate.subdivision.controll-with-but.ng-pristine.ng-untouched.ng-valid.ng-not-empty')
        assert self.check_atribut_text(naimenovanie_rabochego_sentra, 'value', 'Группа ИЛИМ\Братск\Вспом. структурные подразделения\Пр-во по водопод.и инж.коммуник.\Цех очистных сооружений промстоков\Иловая станция №1'), 'Наименование рабочего центра не совпадает'
        checkbox_prichini_sobitia = self.browser.find_elements(By.CSS_SELECTOR, '.checkbox-wrap.small.pull-left label span')
        checkbox_prichini_sobitia[2].click()
        sefe_and_close_button = self.browser.find_elements(By.CSS_SELECTOR, '.modal-button.pull-right .ui-button-text')
        sefe_and_close_button[2].click()
        event_creation_massage = self.browser.find_element(By.CSS_SELECTOR, '#toast-container .toast.toast-success')
        assert self.check_text(event_creation_massage, 'Событие успешно создано'), 'Нет сообщения о создании события через кнопку Создать событие'
        
    def new_event_in_tl_from_menu(self):
        open_group_ilim = self.browser.find_element(By.CSS_SELECTOR, '.k-top.k-bot.ng-scope .k-icon.k-i-expand')
        open_group_ilim.click()
        time.sleep(1)
        open_bratsk = self.browser.find_element(By.CSS_SELECTOR, '.k-bot .k-icon.k-i-expand')
        open_bratsk.click()
        time.sleep(1)
        open_vspom_struktur_podrasdel = self.browser.find_element(By.CSS_SELECTOR, '.k-top .k-icon.k-i-expand')
        open_vspom_struktur_podrasdel.click()
        time.sleep(1)
        open_prvo_po_vodopod_i_ing_kommunic = self.browser.find_element(By.CSS_SELECTOR, '.k-top .k-icon.k-i-expand')
        open_prvo_po_vodopod_i_ing_kommunic.click()
        time.sleep(1)
        open_seh_ochis_sooruzh_promstokov = self.browser.find_element(By.CSS_SELECTOR, '.k-bot .k-icon.k-i-expand')
        open_seh_ochis_sooruzh_promstokov.click()
        time.sleep(1)        
        click_ilovai_stantsia_1 = self.browser.find_elements(By.CSS_SELECTOR, '.k-mid .k-in .tl-item-table tbody tr .ng-binding')
        self.right_click(click_ilovai_stantsia_1[2])        
        time.sleep(1)
        create_event_button = self.browser.find_element(By.CSS_SELECTOR, '.elem a')
        create_event_button.click()
        shablon_event_button = self.browser.find_element(By.ID, '019fa8f1-3475-48b6-bc76-cd05fb357f2f')
        shablon_event_button.click()
        time.sleep(1)
        naimenovanie_rabochego_sentra = self.browser.find_element(By.CSS_SELECTOR, '.standart-input-styles.to-validate.subdivision.controll-with-but.ng-pristine.ng-untouched.ng-valid.ng-not-empty')
        assert self.check_atribut_text(naimenovanie_rabochego_sentra, 'value', 'Группа ИЛИМ\Братск\Вспом. структурные подразделения\Пр-во по водопод.и инж.коммуник.\Цех очистных сооружений промстоков\Иловая станция №1'), 'Наименование рабочего центра не совпадает'
        checkbox_prichini_sobitia = self.browser.find_elements(By.CSS_SELECTOR, '.checkbox-wrap.small.pull-left label span')
        checkbox_prichini_sobitia[2].click()
        sefe_and_close_button = self.browser.find_elements(By.CSS_SELECTOR, '.modal-button.pull-right .ui-button-text')
        sefe_and_close_button[2].click()
        event_creation_massage = self.browser.find_element(By.CSS_SELECTOR, '#toast-container .toast.toast-success')
        print(event_creation_massage.text)
        assert self.check_text(event_creation_massage, 'Событие успешно создано'), 'Нет сообщения о создании события через меню'
        
        

        



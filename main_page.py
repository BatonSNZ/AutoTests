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

    def open_create_new_event_shablon_shablonich(self): #Открытие крточки нового события через кнопку "Создать событие"
        create_event_button = self.browser.find_element(By.ID, 'addEventBtnId')
        create_event_button.click()
        shablon_event_button = self.browser.find_element(By.ID, '019fa8f1-3475-48b6-bc76-cd05fb357f2f')
        shablon_event_button.click()
        assert self.is_element_present(By.CSS_SELECTOR,'[value="ВЫБРАТЬ..."]'), "Карточка события не открылась или там ошибка"
    
    def enter_data_into_event_shablon_shablonich(self): #Заполнение карточки события Шаблон Шаблоныч        
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
        event_creation_message = self.browser.find_element(By.CSS_SELECTOR, '#toast-container .toast.toast-success')
        assert self.check_text(event_creation_message, 'Событие успешно создано'), 'Нет сообщения о создании события через кнопку Создать событие'

    def enter_data_into_event_prostoi_oborudovania(self): #Заполнение карточки события Простой оборудования
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
        button_comment = self.browser.find_element(By.CSS_SELECTOR, '.fa.fa-plus.btn-comment.pull-right')
        button_comment.click()
        comment_area = self.browser.find_element(By.CSS_SELECTOR, '.to-validate.ng-pristine.ng-empty.ng-invalid.ng-invalid-required.ng-touched')
        comment_area.clear()
        comment_area.send_keys("Auto test №123")
        button_self_comment = self.browser.find_element(By.ID, 'confirmComment_a43f4cb3-04ae-4eb3-3fd7-d56ebed4c5a0')
        button_self_comment.click()
        checkbox_prichini_sobitia = self.browser.find_elements(By.CSS_SELECTOR, '.checkbox-wrap.small.pull-left label span')
        checkbox_prichini_sobitia[2].click()
        sefe_and_close_button = self.browser.find_elements(By.CSS_SELECTOR, '.modal-button.pull-right .ui-button-text')
        sefe_and_close_button[2].click()
        event_creation_message = self.browser.find_element(By.CSS_SELECTOR, '#toast-container .toast.toast-success')
        assert self.check_text(event_creation_message, 'Событие успешно создано'), 'Нет сообщения о создании события через кнопку Создать событие'

        
    def new_event_in_tl_from_menu(self): #Открытие карточки события Шаблон Шаблоныч через меню
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
        
    def enter_data_into_event_shablon_shablonich_no_work_center(self): #Заполнение карточки события Шаблон Шаблоныч после открытия через меню
        checkbox_prichini_sobitia = self.browser.find_elements(By.CSS_SELECTOR, '.checkbox-wrap.small.pull-left label span')
        checkbox_prichini_sobitia[2].click()
        sefe_and_close_button = self.browser.find_elements(By.CSS_SELECTOR, '.modal-button.pull-right .ui-button-text')
        sefe_and_close_button[2].click()
        event_creation_message = self.browser.find_element(By.CSS_SELECTOR, '#toast-container .toast.toast-success')        
        assert self.check_text(event_creation_message, 'Событие успешно создано'), 'Нет сообщения о создании события через меню'

    def check_auto_open_menu(self): #Проверка автораскрытия меню до выбранного элемента        
        work_center_selection_button = self.browser.find_element(By.CSS_SELECTOR, '[value="ВЫБРАТЬ..."]')
        work_center_selection_button.click()
        time.sleep(5)
        checkbox_ilovai_stantsia_1 = self.browser.find_element(By.ID, 'checkbox_40ea6f89-9931-11eb-8da9-00155d252971')
        print(checkbox_ilovai_stantsia_1.get_attribute('class'))
        assert self.check_atribut_text(checkbox_ilovai_stantsia_1, 'class', 'ng-pristine ng-untouched ng-valid ng-not-empty'), 'Нет автораскрытия меню'

    def open_event_frame(self): #Открытие карточки события
        event_frame = self.browser.find_element(By.CSS_SELECTOR, '.table-structure-line')
        self.double_click(event_frame)
        time.sleep(1)
        assert self.is_element_present(By.CSS_SELECTOR,'[value="ВЫБРАТЬ..."]'), "Карточка события не открылась или там ошибка"

    def change_event_frame(self): #Внесение изменений в карточку события 
        open_name_equipmqnt = self.browser.find_element(By.CSS_SELECTOR, '[name="Values[094b518e-d731-4082-a316-91a622936c8e].Value_input"]')
        open_name_equipmqnt.clear()
        open_name_equipmqnt.send_keys("1")
        time.sleep(1)
        open_name_equipmqnt.send_keys(Keys.ENTER)        
        sefe_and_close_button = self.browser.find_elements(By.CSS_SELECTOR, '.modal-button.pull-right .ui-button-text')
        sefe_and_close_button[2].click()
        event_change_messege = self.browser.find_element(By.CSS_SELECTOR, '#toast-container .toast.toast-success .toast-message')
        assert self.check_text(event_change_messege, 'Событие успешно обновлено'), 'Ошибка при сохранении изменений'

    def check_change_in_event(self): #Проверка изменений в карточке события во вкладке История
        open_history = self.browser.find_elements(By.CSS_SELECTOR, '.k-item.k-state-default')        
        open_history[1].click()
        time.sleep(1)        
        open_history[2].click()                     
        check_new_value = self.browser.find_elements(By.CSS_SELECTOR, '[role="gridcell"] .ng-binding')
        time.sleep(1)       
        assert self.check_text(check_new_value[1], '1 секция транспортёра'), 'Изменения не появились во вкладке История'

    def create_attach_event(self): #Открытие окна регистранции вложенного события
        checkbox_event = self.browser.find_elements(By.CSS_SELECTOR, '.info-cell-first-column .checkbox-wrap.small')
        checkbox_event[0].click()
        create_event_button = self.browser.find_element(By.ID, 'addEventBtnId')
        create_event_button.click()
        shablon_event_button = self.browser.find_element(By.ID, '5a3afb04-e2b1-4b57-a145-aa10b2605b49')
        shablon_event_button.click()
        assert self.is_element_present(By.CSS_SELECTOR,'[value="ВЫБРАТЬ..."]'), "Карточка события не открылась или там ошибка"

    def check_attach_event_create(self): #Проверка вложенности события во вкладке Связи
        arrow = self.browser.find_element(By.CSS_SELECTOR, '.table-structure-line .k-icon.k-i-expand')
        arrow.click()
        attach_event = self.browser.find_elements(By.CSS_SELECTOR, '.table-structure-line .space')
        self.double_click(attach_event[1])
        open_connect = self.browser.find_elements(By.CSS_SELECTOR, '.k-item.k-state-default')        
        open_connect[2].click()
        time.sleep(1)        
        open_connect[1].click()
        text_connect = self.browser.find_elements(By.CSS_SELECTOR, '.header .title')
        time.sleep(1)
        assert self.check_text(text_connect[1], 'Приёмник: от других событий к этому'), 'Нет связи во вкладке Связи'

    def add_investments(self): #Добавление вложения 
        open_event = self.browser.find_elements(By.CSS_SELECTOR, '.table-structure-line .space')
        self.double_click(open_event[0])
        open_invest = self.browser.find_elements(By.CSS_SELECTOR, '.k-item.k-state-default')        
        open_invest[2].click()
        time.sleep(1)        
        open_invest[3].click()
        


        


        
        

        



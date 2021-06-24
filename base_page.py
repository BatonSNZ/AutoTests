import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

import os

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
           self.browser.find_element(how, what)
        except (NoSuchElementException):
           return False
        return True 

    def is_element_present_with_waiting(self, how, what):
        try:
            WebDriverWait(self.browser, 60).until_not(EC.invisibility_of_element((how, what)))
        except:
           return False
        return True   
    
    def is_element_no_present(self, how, what):
        try:
            WebDriverWait(self.browser, 1).until(EC.NoSuchElementException((how, what)))
        except:
           return True
        return False

    def is_element_text_wating(self, element, text):
        while element.text != text:   
            time.sleep(1)
        else:
            return True

    def is_element_no_text_wating(self, element, text):
        while element.text == text:   
            time.sleep(1)
        else:
            return True        

    def is_element_invisibility(self, how, what):
        try:
            WebDriverWait(self.browser, 10).until(EC.invisibility_of_element((how, what)))
        except:
           return False
        return True         

    def check_atribut_text(self, element, attribute_name, text):
        if element.get_attribute(attribute_name) == text:   
            return True
        else:
            return False

    def check_text(self, element, text):
        if element.text == text:   
            return True
        else:
            return False

    def check_text_not(self, element, text):
        if element.text != text:   
            return True
        else:
            return False

    def right_click(self, here):       
        action = ActionChains(self.browser)
        action.context_click(on_element = here).perform()

    def double_click(self, here):       
        action = ActionChains(self.browser)
        action.double_click(on_element = here).perform()

    def refresh_page(self):
        self.browser.refresh()

    def enter_file(self, file):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, file)
        return file_path

    def check_list_eq(self, list, long, text):
        i = 0
        while i < long:
            if list[i].text == text: 
                i += 1  
            else:
                return False
        else:
                return True    

    def check_list_no_eq(self, list, long, text):
        i = 0
        while i < long:
            if list[i].text != text: 
                i += 1  
            else:
                return False
        else:
                return True 

    def check_list_no_eq_not_0(self, list, long, text):
        i = 2
        while i < long:
            if list[i].text != text: 
                i += 16  
            else:
                return False
        else:
                return True     

    def check_list_for_kvit(self, list, long, namber1, namber2, text1, text2):
        i = 2
        j = 0
        g = 0
        while i < long:
            while j != namber1:
                if list[i].text == text1: 
                    i += 16
                    j += 1  
                else:
                    return False
            while g != namber2:
                if list[i].text == text2: 
                    i += 16  
                    g += 1
                else:
                    return False        
        else:
            return True

    def check_list_for_status_code(self, list, long):
        i = 0
        while i < long - 1:
            if int(list[i].text) >= int(list[i+1].text): 
                i += 1  
            else:
                return False
        else:
                return True   

    def check_list_start_date(self, list, long):
        i = 3 
        j = 0       
        list_date = []
        while i < long:            
            list_date.append(datetime.strptime(list[i].text, "%d.%m.%Y %H:%M:%S"))
            i += 23
        while j < len(list_date) - 1:
            if list_date[j] >= list_date[j + 1]: 
                j += 1  
            else:
                return False
        else:
                return True              
           

             

                   

       
        
            
        


        
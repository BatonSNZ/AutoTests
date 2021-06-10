from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    

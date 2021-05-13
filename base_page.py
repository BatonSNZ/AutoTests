from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url, timeout=5):
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
        
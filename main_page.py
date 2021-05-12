from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MainPage(BasePage):
    def in_to_login(self):
        username_fild = self.browser.find_element(By.ID, 'txtUserName')
        username_fild.clear()
        username_fild.send_keys("sam")
        password_fild = self.browser.find_element(By.ID, 'txtPassword')
        password_fild.clear()
        password_fild.send_keys("sam")
        enter_button = self.browser.find_element(By.CLASS_NAME, 'btn-login')
        enter_button.click()

    def should_be_start_page(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Не авторизовался"    

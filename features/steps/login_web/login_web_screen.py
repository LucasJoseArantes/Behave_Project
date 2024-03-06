from features.helpers.selenium_helpers import navigate_to_url, assert_word_in_message , assert_message_matches , assert_redirect_url , wait_element, click_element 

from features.common.element_locators import SELECTORS
from features.common.constants import info

class LoginWebScreen:
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.login_username_input_selector = SELECTORS["login"]["username_input"]
        self.login_password_input_selector = SELECTORS["login"]["password_input"]
        self.login_submit_button_selector = SELECTORS["login"]["submit_button"]
        self.login_logged_in_successfully_message_selector = SELECTORS["login"]["logged_in_successfully_message"]
        self.login_log_out_button_selector = SELECTORS["login"]["log_out_button"]
        self.login_invalid_credentials_message_selector = SELECTORS["login"]["invalid_credentials_message"]

    def navigate_to_login_screen(self, login_url):
        navigate_to_url(self.webdriver, login_url)  
    
    def check_acessed_login_screen(self, login_url):
        assert_redirect_url(self.webdriver, login_url)

    def set_input_username_login(self, username):
        username_input = wait_element(self.webdriver, self.login_username_input_selector)
        username_input.send_keys(username)

    def set_input_password_login(self, password):
        password_input = wait_element(self.webdriver, self.login_password_input_selector)
        password_input.send_keys(password)

    def click_button_login(self):
        click_element(self.webdriver, self.login_submit_button_selector)

    def check_logged_in_successfully(self, logged_in_url):
        assert_redirect_url(self.webdriver, logged_in_url)
    
    def check_expected_message_is_present_in_text(self, message):
        assert_word_in_message(self.webdriver, self.login_logged_in_successfully_message_selector, message)
    
    def check_log_out_button(self):
        click_element(self.webdriver, self.login_log_out_button_selector)

    def check_message_on_login_screen(self, message):
        assert_message_matches(self.webdriver, self.login_invalid_credentials_message_selector, message)
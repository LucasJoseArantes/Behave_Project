from features.helpers.selenium_helpers import navigate_to_url

class LoginWebScreen:
    def __init__(self, webdriver):
        self.webdriver = webdriver

    def navigate_to_login_screen(self, login_url):
        navigate_to_url(self.webdriver, login_url)  
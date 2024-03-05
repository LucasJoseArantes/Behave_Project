from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

def get_webdriver():
    # Set Firefox options
    options = Options()
    options.add_argument("--headless")  # Run Firefox in headless mode
    options.add_argument("--disable-notifications") # Disable browser notifications
    options.add_argument("--window-size=1920,1080") # Set window size to 1920x1080

    # Initialize the webdriver with Firefox and options
    webdriver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


    return webdriver


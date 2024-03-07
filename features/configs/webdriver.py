from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager


def get_webdriver():

    # Get the path of the webdriver
    webdriver_path = GeckoDriverManager().install()

    # Set Firefox options
    options = FirefoxOptions()
    # options.add_argument("--headless")  # Run Firefox in headless mode
    options.add_argument("--disable-notifications") # Disable browser notifications

    webdriver_class = webdriver.Firefox

    # Initialize the webdriver with Firefox and options
    driver = webdriver_class(options=options)

    # Maximize the window
    driver.maximize_window()

    return driver


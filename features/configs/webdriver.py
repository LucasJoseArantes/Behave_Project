from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from features.common.constants import BROWSER, HEADLESS_MODE, SERVER


def get_webdriver():
    print("\n========================================= Webdriver Settings ==========================================")
    print(f"Headless mode: {HEADLESS_MODE}")
    print(f"Chosen browser: {BROWSER}")
    print(f"Chosen server: {SERVER}")

    if BROWSER == "chrome":
        webdriver_path = ChromeDriverManager().install()
        print(f"Chrome webdriver path: {webdriver_path}")
        options = ChromeOptions()
        options.add_argument("--lang=pt-BR")
        options.add_experimental_option("prefs", {"enable_do_not_track": True})
        webdriver_class = webdriver.Chrome

    else:
        webdriver_path = GeckoDriverManager().install()
        print(f"Webdriver path: {webdriver_path}")
        profile = FirefoxProfile()
        profile.set_preference("intl.accept_languages", "pt-BR")
        profile.set_preference("privacy.trackingprotection.enabled", True)
        options = FirefoxOptions()
        options.profile = profile
        webdriver_class = webdriver.Firefox

    if HEADLESS_MODE:
        options.add_argument("--headless")

    driver = webdriver_class(options=options)
    driver.maximize_window()

    window_size = driver.get_window_size()
    print(f"Screen resolution: {window_size}")
    print("=======================================================================================================\n")

    return driver


from os import environ

from common.users import USERS_STAGE

ENVIRONMENTS_DATA = {
    "stage": {
        "users": USERS_STAGE,
        "login_screen": "https://practicetestautomation.com/practice-test-login/",
        "logged_in_successfully_screen": "https://practicetestautomation.com/logged-in-successfully/",
    }
}

SERVER = environ.get("ENV", "stage")
HEADLESS_MODE = environ.get("HEADLESS_MODE", "False").lower() not in ("false", "0", "f")
BROWSER = environ.get("BROWSER", "firefox")
info = ENVIRONMENTS_DATA[SERVER]
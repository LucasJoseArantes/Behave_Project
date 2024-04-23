from os import environ

from common.adress import ADRESS_DATA
from common.url_requests import URL_REQUESTS
from common.users import USERS_STAGE

ENVIRONMENTS_DATA = {
    "stage": {
        "users": USERS_STAGE,
        "login_screen": "https://practicetestautomation.com/practice-test-login/",
        "logged_in_successfully_screen": "https://practicetestautomation.com/logged-in-successfully/",
        "url_requests": URL_REQUESTS,
        "adress_data": ADRESS_DATA,
    }
}

SERVER = environ.get("ENV", "stage")
HEADLESS_MODE = environ.get("HEADLESS_MODE", "False").lower() not in ("false", "0", "f")
BROWSER = environ.get("BROWSER", "firefox")
info = ENVIRONMENTS_DATA[SERVER]

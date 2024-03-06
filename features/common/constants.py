from os import environ
from common.users import USERS_STAGE

ENVIRONMENTS_DATA = {
    "stage": {
        "users": USERS_STAGE,
        "login_screen": "https://practicetestautomation.com/practice-test-login/",
        "logged_in_successfully_screen": "https://practicetestautomation.com/logged-in-successfully/",
    }
}

ENV = environ.get("ENV", "stage")
info = ENVIRONMENTS_DATA[ENV]
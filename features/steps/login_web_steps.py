from behave import given, then, when
from common.constants import info
from features.steps.login_web_screen import LoginWebScreen

@given("I access the login screen")
def step_acess_login_screen(context):
    login_web_screen = LoginWebScreen(context.webdriver)
    login_web_screen.navigate_to_login_screen(info["login_screen"])
    # login_web_screen.check_acessed_login_screen()

@when("I type '{}' user credentials into the login form")
def step_type_user_credentials(context, user):
    login_web_screen = LoginWebScreen(context.webdriver)
    login_web_screen.set_input_username_login(info["users"][user]["username"])
    login_web_screen.set_input_password_login(info["users"][user]["password"])

@when("I click on the login button")
def step_click_login_button(context):
    login_web_screen = LoginWebScreen(context.webdriver)
    login_web_screen.click_button_login()

@then("I should be redirected to the logged in successfully screen")
def step_check_logged_in_successfully(context):
    login_web_screen = LoginWebScreen(context.webdriver)
    login_web_screen.check_logged_in_successfully()

@then("I should see the message on the logged in successfully screen")
def step_check_logged_in_successfully_message(context):
    login_web_screen = LoginWebScreen(context.webdriver)
    login_web_screen.check_logged_in_successfully_message()

@then("I should see the log out button displayed on the logged in successfully screen")
def step_check_log_out_button(context):
    login_web_screen = LoginWebScreen(context.webdriver)
    login_web_screen.check_log_out_button()

@then('I should see the message "{message}" on the login screen')
def step_check_message_on_login_screen(context, message):
    login_web_screen = LoginWebScreen(context.webdriver)
    login_web_screen.check_message_on_login_screen(message)
from behave import given, then, when
from common.constants import info
from steps.login_web_screen import LoginWebScreen

def setup_login_web_screen(context):
    context.login_web_screen = LoginWebScreen(context.webdriver)

@given("I access the login screen")
def acess_login_screen(context):
    setup_login_web_screen(context)
    context.login_web_screen.navigate_to_login_screen()
    context.login_web_screen.check_acessed_login_screen()

@when("I type '{user}' user credentials into the login form")
def type_user_credentials(context, user):
    setup_login_web_screen(context)
    context.login_web_screen.set_input_username_login(info["users"][user]["username"])
    context.login_web_screen.set_input_password_login(info["users"][user]["password"])

@when("I click on the login button")
def click_login_button(context):
    setup_login_web_screen(context)
    context.login_web_screen.click_button_login()

@then("I should be redirected to the logged in successfully screen")
def check_logged_in_successfully(context):
    setup_login_web_screen(context)
    context.login_web_screen.check_logged_in_successfully()

@then("I should see the message on the logged in successfully screen")
def check_logged_in_successfully_message(context):
    setup_login_web_screen(context)
    context.login_web_screen.check_logged_in_successfully_message()

@then("I should see the log out button displayed on the logged in successfully screen")
def check_log_out_button(context):
    setup_login_web_screen(context)
    context.login_web_screen.check_log_out_button()

@then('I should see the message "{message}" on the login screen')
def check_message_on_login_screen(context, message):
    setup_login_web_screen(context)
    context.login_web_screen.check_message_on_login_screen(message)

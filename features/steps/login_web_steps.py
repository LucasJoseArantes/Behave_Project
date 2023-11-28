from behave import then, when, given
import web_common
from configs.locatorsconfig import MY_ACCOUNT_LOCATORS
import pdb

@given ("I go to '{page}' page")
def go_to_page(context, page):
    context.driver = web_common.go_to(context, page)

@when("I type '{email}' into username of login form")
def type_email_into_username_f_login_form(context, email):

    email_locator_type = MY_ACCOUNT_LOCATORS['login']['login_username']['type']
    email_locator_string = MY_ACCOUNT_LOCATORS['login']['login_username']['locator']

    web_common.type_into_element(context, str(email) , email_locator_type , email_locator_string )

@when("I type '{password}' into password of login form")
def type_pssword_into_username_f_login_form(context, password):

    password_locator_type = MY_ACCOUNT_LOCATORS['login']['login_password']['type']
    password_locator_string = MY_ACCOUNT_LOCATORS['login']['login_password']['locator']

    web_common.type_into_element(context, str(password) , password_locator_type , password_locator_string )

@when("I click on the 'login' button")
def click_btn_in_f_login_form(context):

    login_btn_locator_type = MY_ACCOUNT_LOCATORS['login']['login-btn']['type']
    login_btn_locator_string = MY_ACCOUNT_LOCATORS['login']['login-btn']['locator']

    web_common.click(context,login_btn_locator_type, login_btn_locator_string )

    pdb.set_trace()

@then("I should see {user} displayed in the login message")
def user_should_be_logged_in(context, user):
    
    success_message_locator_type = MY_ACCOUNT_LOCATORS['logged-in-successfully']['success_message_username']['type']
    success_message_locator_string = MY_ACCOUNT_LOCATORS['logged-in-successfully']['success_message_username']['locator']

    website_message = web_common.get_element_text(context,success_message_locator_type, success_message_locator_string )

    print('++++++++++++++++++++++++++++++++')
    print('############ Expected Username: ' + user )
    print('############ Website Username: ' + website_message )
    print('++++++++++++++++++++++++++++++++')
    pdb.set_trace()

    if(website_message.lower() != user.lower()):
        raise AssertionError(f"Os nomes não coincidem. Esperado: '{user}', Obtido: '{website_message}'")

# @then("I should see the log out button displayed on the logged in successfully screen")
# def step_should_see_the_button_displayed(context):


from behave import given, when, then

from features.common.constants import info


from features.steps.api.api import ApiInterface

@given("I make a GET request using '{}' url")
def step_make_get_request( context, get_url):
    api_interface = ApiInterface()
    # context.response = api_interface.make_get_adress_request(info["url_requests"][get_url])
    context.response = api_interface.make_get_adress_request(info["url_requests"][get_url])

@then("I should receive a successful response")
def step_check_receive_successful_response(context):
    api_interface = ApiInterface()
    api_interface.check_response_status_code(context.response.status_code, 200)
    

@then("I check the adress response")
def step_check_adress_response(context):
    api_interface = ApiInterface()
    response_json = context.response.json()
    filter_adress = {
        'logradouro': response_json['logradouro'],
        'bairro': response_json['bairro'],
        'localidade': response_json['localidade']
    }
    api_interface.check_adress_response(filter_adress, info["adress_data"])

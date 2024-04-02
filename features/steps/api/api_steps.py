from behave import given, when, then
from features.helpers.api_helpers import _make_request 

from features.common.constants import info

from features.steps.api.api import ApiInterface

@given("I make a GET request using '{}' url")
def step_make_get_request( context, get_url):
    api_interface = ApiInterface()
    context.response = api_interface.make_get_adress_request(info["url_requests"][get_url].format('01310200'))

@given("I make a '{}' request using '{}' url")
def step_make_request( context, method, url):
    api_interface = ApiInterface()
    if method == "DELETE" : json_data = None
    else : json_data = api_interface.convert_adress_data_to_json(info["adress_data"])
    context.response = _make_request(url=info["url_requests"][url] , context=context, method=method , data=json_data)

@then("I check the JSON response")
def step_check_json_response(context):
    api_interface = ApiInterface()
    api_interface.get_json_response(context.response)
    

@then("I should receive a successful response")
def step_check_receive_successful_response(context):
    api_interface = ApiInterface()
    api_interface.check_response_status_code(context.response.status_code, 200)
    
@then("I check the JSON response matches the schema")
def step_check_json_response(context):
    api_interface = ApiInterface()
    response_json = context.response.json()
    filter_adress = {
        'Adress Test': {	 
        'logradouro': response_json['logradouro'],
        'bairro': response_json['bairro'],
        'localidade': response_json['localidade']
        }
    }
    api_interface.check_adress_response(filter_adress, info["adress_data"])

from features.helpers.api_helpers import _make_request

class ApiInterface:
    def make_get_adress_request(context, url):
        return _make_request(url, context , "GET")
    
    def check_response_status_code(self, response, expected_status_code):
        assert response == expected_status_code, f"Expected status code {expected_status_code}, but got {response}"

    def check_adress_response (response_json_adress, expected_adress)
    

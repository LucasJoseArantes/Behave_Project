from features.helpers.api_helpers import _make_request
import logging as log


class ApiInterface:
    def make_get_adress_request(context, url):
        return _make_request(url, context , "GET")
    
    def check_response_status_code(self, response, expected_status_code):
        log.info(f"Response status code: {response}")
        assert response == expected_status_code, f"Expected status code {expected_status_code}, but got {response}"

    def check_adress_response(self, response_json_adress, expected_adress):
        log.info(f"Response json: {response_json_adress}")
        assert response_json_adress == expected_adress, f"Expected adress {expected_adress}, but got {response_json_adress}"
        
    

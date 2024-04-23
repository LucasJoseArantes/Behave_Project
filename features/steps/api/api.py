import json
import logging as log

from features.helpers.api_helpers import _make_request, format_string


class ApiInterface:
    def make_get_adress_request(context, url):
        return _make_request(url, context, "GET", "")

    def check_response_status_code(self, response, expected_status_code):
        log.info(f"Response status code: {response}")
        assert response == expected_status_code, f"Expected status code {expected_status_code}, but got {response}"

    def check_adress_response(self, response_json_adress, expected_adress):
        for key, value in response_json_adress.items():
            response_json_adress[key] = format_string(value)
        log.info(f"Expected json: {expected_adress}")
        log.info(f"Response json: {response_json_adress}")
        assert (
            response_json_adress == expected_adress
        ), f"Expected adress {expected_adress}, but got {response_json_adress}"

    def convert_adress_data_to_json(self, data):
        try:
            # Convert the dictionary to a JSON string keeping non-ASCII characters
            json_data = json.dumps(data, indent=4, ensure_ascii=False)
            log.info(f"Formated data to JSON:\n{json_data}")
            return json_data
        except Exception as e:
            log.error(f"Error converting data to JSON: {e}")
            raise

    def get_json_response(self, response):
        try:
            json_response = response.json()
            log.info(f"Response json:\n{json_response}")
            return json_response
        except Exception as e:
            log.error(f"Error getting JSON response: {e}")
            raise

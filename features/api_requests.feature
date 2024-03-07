Feature: Testing API Requests

    Scenario: Successful GET request
        Given I set the API URL as '<get_url>'  
        When I make a GET request to the API
        Then I should receive a successful response
        And the response should be in JSON format

    Scenario: Successful POST request
        Given I set the API URL as '<post_url>'
        When I make a POST request to the API
        Then I should receive a successful response

    Scenario Outline: Invalid API key should return 401
        Given I set the API URL as "<>"
        When I make a POST request to the API
        And I set an '<invalid_key>'
        Then I should receive a 401 Unauthorized response

        Examples:
        | invalid_key |
        | invalid_key_1 |
        | invalid_key_2 |

    Scenario Outline: Resource not found should return 404
        Given I set the API URL as "<>"
        When I make a GET request to the API
        And I set a non-existing '<resource>'
        Then I should receive a 404 Not Found response

        Examples:
        | resource |
        | resource_1 |
        | resource_2 |




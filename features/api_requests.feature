Feature: Testing API Requests

    Scenario: Successful GET request
        Given I make a GET request using 'get_url' url
        Then I should receive a successful response
        And I check the JSON response

    Scenario: Successful POST request
        Given I make a POST request using 'post_url' url
        Then I should receive a successful response
        # And I check the JSON response

    # Scenario Outline: Invalid API key should return 401
    #     Given I set the API URL as "<>"
    #     When I make a POST request to the API
    #     And I set an '<invalid_key>'
    #     Then I should receive a 401 Unauthorized response

    #     Examples:
    #     | invalid_key |
    #     | invalid_key_1 |
    #     | invalid_key_2 |



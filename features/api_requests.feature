Feature: Testing API Requests

    Scenario: Get user adreess using Correios API
        Given I make a GET request using 'get_adress' url 
        Then I should receive a successful response
        And I check the JSON response matches the schema

    Scenario: Post user adreess using Firebase API
        Given I make a 'POST' request using 'firebase_post_url' url
        Then I should receive a successful response
        And I check the JSON response

    Scenario: Patch user adreess using Firebase API
        Given I make a 'PATCH' request using 'firebase_patch_url' url
        Then I should receive a successful response
        And I check the JSON response

    Scenario: Delete user adreess using Firebase API
        Given I make a 'DELETE' request using 'firebase_delete_url' url
        Then I should receive a successful response

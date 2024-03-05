@web_ui
Feature: Login screen tests

  Background: Prepare the environment
    Given I access the login screen

    Scenario: Valid user should be able to login
        When I type 'first' user credentials into the login form
        And I click on the login button
        Then I should be redirected to the logged in successfully screen
        And I should see the message on the logged in successfully screen
            | message                 |
            | Congratulations         |
            | successfully logged in  |
        And I should see the log out button displayed on the logged in successfully screen
    
    Scenario Outline: Invalid user shouldn't be able to login
        When I type 'second' user credentials into the login form
        And I click on the login button
       Then I should see the message "<message>" on the login screen

    Examples:
      | user    | message                     |
      | second  | Your username is invalid!   |
      | third   | Your password is invalid!   |
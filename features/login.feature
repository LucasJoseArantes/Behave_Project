@my_account_smoke

Feature: My Account Smoke Test

    Background: Prepare the environment
        Given I go to 'my account' page

    Scenario: Valid user should be able to login
        When I type 'lucasteste123@gmail.com' into username of login form
        And I type 'lucasteste123@senha' into password of login form
        And I click on the 'login' button
        Then I should see lucasteste123 displayed in the login message 
        And I should see the log out button displayed on the logged in successfully screen
        
                
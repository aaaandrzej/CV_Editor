Feature: Use get method on identify endpoint and see the user details
  Scenario: Use a get method on identify endpoint
    Given an app is running
    And db is up
    And db contains a user record
    When user requests new token
    And user uses get method with token attached on identify endpoint
    Then they should receive a "200" status code
    And a message response is json with admin user details
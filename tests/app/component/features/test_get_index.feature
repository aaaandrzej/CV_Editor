Feature: Use get method on index endpoint and see the info message
  Scenario: Use a get method on index endpoint
    Given an app is running
    When user uses "get" method "without" token attached on "index" endpoint
    Then they should receive a "200" status code
    And a message response is "For API please use /api/cv or /api/cv/<id>"
Feature: Request get_secret() function to obtain DB password from Secrets Manager
  Scenario: Request get_secret() function to obtain DB password from Secrets Manager
    Given localstack is running
    When user uses get secret method
    Then they should receive a "dupa" response
Feature: Endpoint api_cv_post
Scenario Outline: Use post method on api_cv_post endpoint and verify if response is valid
    Given an app is still running
    When user sends "<json_input>" query
    Then they should get a "<status_code>" status code
    And a response message is "<response>"

Examples:
| json_input | status_code | response                    |
| {}         | 201         | {"success": "item added"}   |

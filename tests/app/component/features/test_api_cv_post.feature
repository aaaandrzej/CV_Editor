Feature: Endpoint api_cv_post

Scenario Outline: Use post method on api_cv_post endpoint and verify if response is positive
    Given an app is running
    And db is up
    And db contains "admin" record
    And user requests new token
    When admin user sends "<json_file>" query
    Then they should receive a "<status_code>" status code
    And a message response is json with user details
    And "<json_file>" content is present in database

Examples:
| json_file  | status_code |
| 201-1.json | 201         |
| 201-2.json | 201         |
| 201-3.json | 201         |
| 201-4.json | 201         |
| 201-5.json | 201         |


@negative
Scenario Outline: Use post method on api_cv_post endpoint and verify if response is error
    Given an app is running
    And db is up
    And db contains "admin" record
    And user requests new token
    When admin user sends "<json_file>" query
    Then they should receive a "<status_code>" status code
    And a message response is "<response>"

Examples:
| json_file  | status_code | response                    |
| 400-1.json | 400         | {"error": "bad input data"} |
| 400-2.json | 400         | {"error": "bad input data"} |
| 400-3.json | 400         | {"error": "bad input data"} |
| 400-4.json | 400         | {"error": "bad input data"} |


@negative
Scenario Outline: Use post method on api_cv_post endpoint and verify that access is denied
    Given an app is running
    And db is up
    And db contains "admin" record
    When admin user sends "<json_file>" query
    Then they should receive a "<status_code>" status code
    And a message response is "<response>"

Examples:
| json_file  | status_code | response                       |
| 201-1.json | 401         | {"message": "token is invalid"}|
| 400-1.json | 401         | {"message": "token is invalid"}|



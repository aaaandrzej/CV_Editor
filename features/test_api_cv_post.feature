Feature: Endpoint api_cv_post
Scenario Outline: Use post method on api_cv_post endpoint and verify if response is valid
    Given an app is still running
    When user sends "<json_file>" query
    Then they should get a "<status_code>" status code
    And a response message is "<response>"
    And "<json_file>" content should be present in database

Examples:
| json_file  | status_code | response                    |
| 201-1.json | 201         | {"success": "item added"}   |
| 201-2.json | 201         | {"success": "item added"}   |
| 201-3.json | 201         | {"success": "item added"}   |
| 201-4.json | 201         | {"success": "item added"}   |
| 201-5.json | 201         | {"success": "item added"}   |
| 400-1.json | 400         | {"error": "bad input data"} |
| 400-2.json | 400         | {"error": "bad input data"} |
| 400-3.json | 400         | {"error": "bad input data"} |
| 400-4.json | 400         | {"error": "bad input data"} |


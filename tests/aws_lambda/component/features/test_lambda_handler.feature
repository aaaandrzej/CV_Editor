Feature: Lambda handler

Scenario Outline: Use lambda handler function and verify if response is positive
    Given localstack is running
    And DB is up
    When user sends "<json_file>" query
    Then they should get a "<response>" response
    And "<json_file>" content is present in database

Examples:
| json_file  | response                                                                                                |
| 201-1.json | {'statusCode': 200, 'body': '{"firstname": "Test", "lastname": "1", "skills": [], "experience": []}'}   |
| 201-2.json | {'statusCode': 200, 'body': '{"firstname": "Second Test", "lastname": "User", "skills": [{"skill_name": "skill1", "skill_level": 1}, {"skill_name": "skill2", "skill_level": 2}], "experience": [{"company": "Firma", "project": "Project", "duration": 5}]}'}  |
| 201-3.json | {'statusCode': 200, 'body': '{"firstname": "3rd Test", "lastname": "User", "skills": [], "experience": [{"company": "Firma", "project": "Project", "duration": 5}]}'} |
| 201-4.json | {'statusCode': 200, 'body': '{"firstname": "Another test", "lastname": "User", "skills": [], "experience": [{"company": "Firma", "project": "Project", "duration": 5}, {"company": "Firma2", "project": "Project", "duration": 5}, {"company": "Firma3", "project": "Project", "duration": 5}]}'} |
| 201-5.json | {'statusCode': 200, 'body': '{"firstname": "no exp", "lastname": "user", "skills": [], "experience": []}'}  |


@negative
Scenario Outline: Use post method on api_cv_post endpoint and verify if response is error
    Given localstack is running
    When user sends "<json_file>" query
    Then they should get a "<response>" response

Examples:
| json_file  | response                    |
| 400-1.json | {'statusCode': 400, 'body': '"bad input in event body: {\\"lastname\\": \\"no firstname\\", \\"skills\\": [], \\"experience\\": []}"'} |
| 400-2.json | {'statusCode': 400, 'body': '"bad input in event body: {\\"firstname\\": \\"no lastname\\", \\"skills\\": [], \\"experience\\": []}"'} |
| 400-3.json | {'statusCode': 400, 'body': '"bad input in event body: {\\"firstname\\": \\"no skills\\", \\"lastname\\": \\"User\\", \\"experience\\": [{\\"company\\": \\"Firma\\", \\"project\\": \\"Project\\", \\"duration\\": 5}]}"'} |
| 400-4.json | {'statusCode': 400, 'body': '"bad input in event body: {}"'} |
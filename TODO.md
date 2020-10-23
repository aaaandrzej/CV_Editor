

2020-09-18 

Using packet manager (poetry) 

Creating docker image of an application 

Prepare AWS Lambda implementation and package preparation 

Pack lambda 3rd party library dependencies into Lambda Layer 

<br>


2020-09-25 

Deploy Lambda with layer in AWS using AWS console
 
Configure API Gateway to use the Lambda (AWS console) 

<br>


2020-10-02 

Using AWS services with boto3 (Secrets Manager) for storing DB password 

Mocking AWS services with moto (ut) and localstack (component tests) 

Makefile scripts for building lambda packages & layers

<br>


2020-10-21 

Authorization and authentication (API key, JWT) 
- pass hash + salt
- api key - jwt - username in token
- new user management endpoint (change password functionality)
- individual endpoints should be secured and recognize who is logged in

Unit and component tests for auth

Fix old component tests - they should run on mysql in docker
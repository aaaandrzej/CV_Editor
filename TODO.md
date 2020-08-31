26/08/2020

MySQL migration

Multi table queries 
Aggregation queries 

Input data error handling 
    - zaimplementowac tylko dla post user
    - walidowac dane wejsciowe pod katem poprawnosci - czy sa poprawne klucze
    - nie moze byc 500 w zadnym wypadku
    - w przypadku bledu zwracac 400 + json o wartosci {"error": "bad input data"}
    - bledy nie moga byc luka bezpieczenstwa
    
Pytest (mock, patch, parametrize, fixture) 
    - zaimplementowac tylko dla post user
    
Behave (component tests) 
    - zaimplementowac tylko dla post user

Using packet manager (poetry) 
Creating docker image of an application 
Application deployment in ECS using RDS 
Lambda preparing and deployment using API Gateway and RDS 

Using AWS services with boto3 (SSM, Secrets Manager) 
Mocking AWS services with moto and localstack 
Terraform introduction - optional 

authorization and authentication (API key, JWT) 
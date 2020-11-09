# CV_Editor

#### Python REST API designed to view, add, modify and delete CV entries in database, made for educational purposes only. Use it as you like, but at your own risk.

API endpoints and methods allowed:
- / - GET - basic API info
- /login - GET (Basic Auth required) - if user/pass pair is correct API provides token as json {"token": <JWT token>} valid for 30 minutes
- /identify - GET (Bearer token required) - if token is correct API provides token owner info as json
- /api/cv - GET (no auth required) - API returns JSON with all users and their relevant skills and experience
- /api/cv - POST (Bearer token required, available for admin users only) - accepts JSON and if correct creates user and provides its details in response
- /api/cv/<user_id> - GET - (no auth required) - API returns json with given user details
- /api/cv/<user_id> - PUT - (Bearer token required, available for user_id itself and admin users only) - accepts JSON and if correct updates user and provides its details in response
- /api/cv/<user_id> - DELETE - (Bearer token required, available for and admin users only) - deletes user provided in user_id
- /api/cv/<user_id>/password - POST - (Bearer token required, available for user_id itself and admin users only) - accepts JSON and if correct updates user's password and provides their general details in response
- /api/cv/stats - GET (no auth required) - based on skills provided in JSON returns users from db matching requested profile
- /api/cv/stats/count - GET (no auth required) - based on skills provided in JSON returns number of users from db matching requested profile


Accepted JSON structure:

- CV creation/ modification:
{
    "username": "user",
    "password": "password",
    "firstname": "3",
    "lastname": "User",
    "skills": [
        {
            "skill_name": "sql",
            "skill_level": 20
        },
        {
            "skill_name": "python",
            "skill_level": 2
        },
        {
            "skill_name": "judo",
            "skill_level": 10
        }
    ],
    "experience": [
        {
            "company": "Projekt",
            "project": "Projekt",
            "duration": 1
        }
    ]
}

- password change:
{
    "new_password": "new_password",
    "old_password": "password"
}

- stats and count requests:
[
    {
    "skill_name": "sql",
    "skill_level": 20
    },
    {
    "skill_name": "python",
    "skill_level": 7
    }
]

Sample requests provided in attached postman collection.


### Application dev requirements:

docker-compose or venv with python 3.8 and poetry dependencies listed in pyproject.toml, if you want to run it outside of a docker container

Application by default runs on port 5000 and uses MySQL database hosted on port 3306.
Ports 5001 and 3307 are used for test app and db instances.


### Environment variables required to start app or run tests (via make):
Required:

DB_USER

DB_PASSWORD

DB_NAME

SECRET_KEY

Optional, for creating first user:

APP_USER

APP_PASSWORD

PYTHONPATH=.
 
DB_PORT (DB_PORT=3306)
 
DB_HOST (DB_HOST=localhost)

### Makefile commands - running app:

Start app and production database, assuming you already have any records in your database - otherwise run the app and trigger init-db script listed next here:

`make start-app` 

`(or DB_PASSWORD=password DB_USER=user DB_NAME=my_db SECRET_KEY=secretkey make start-app)`

Trigger db schema migration and first user creation, when starting app for the first time:

`make init-db` 

`(or DB_PASSWORD=password DB_USER=user DB_NAME=my_db APP_USER=admin APP_PASSWORD=password PYTHONPATH=. DB_PORT=3306 DB_HOST=localhost make init-db)`

#### Makefile commands - running tests:

Run unit tests:

`make unittest-app`

Run component tests:

`make component-prep`

`(or DB_PORT=3307 DB_PASSWORD=password DB_USER=user DB_NAME=my_db SECRET_KEY=secretkey make component-prep)`

`alembic upgrade head`

`(or DB_PASSWORD=password DB_USER=user DB_NAME=my_db PYTHONPATH=. DB_PORT=3307 DB_HOST=localhost alembic upgrade head)`

`make component-app`

#### Folder structure
/alembic - alembic configuration and migration files

/app - app files, with main.py being one starting app

/aws_lambda - basic app functionality adopted to work as AWS Lambda with API Gateway, Secrets Manager and MySQL in RDS, not required by the main app anyhow

/tests/app - component and unit tests for the app

/tests/lambda - component and unit tests for the aws_lambda app

<br>

##### Author: andrzej.szulc@gmail.com

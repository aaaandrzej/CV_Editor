BUILD_DIR ?= _build

start-app:
	docker-compose up database app

init-db:
	PYTHONPATH=. alembic upgrade head

unittest-app:
	PYTHONPATH=. pytest tests/app/unit/

component-prep:
	docker-compose up database_test app_test

component-app:
	behave tests/app/component/features/

build-lambda:
	pip install sqlalchemy pymysql -t $(BUILD_DIR)/python
	cp aws_lambda/*.py $(BUILD_DIR)/
	cd $(BUILD_DIR); zip -r9 lambda.zip *.py -x "_temp*.*"
	cd $(BUILD_DIR); zip -r9 layer.zip python
	rm -rf $(BUILD_DIR)/python $(BUILD_DIR)/*.py

unittest-lambda:
	DB_USER=test DB_PASSWORD=test DB_HOST=test DB_PORT=0 DB_NAME=test PYTHONPATH=.:aws_lambda pytest -p no:warnings tests/aws_lambda/unit/

component-lambda:
	PYTHONPATH=.:aws_lambda behave tests/aws_lambda/component/features/

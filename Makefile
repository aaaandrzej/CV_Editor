BUILD_DIR ?= _build

build:
	pip install sqlalchemy pymysql -t $(BUILD_DIR)/python
	cp aws_lambda/*.py $(BUILD_DIR)/
	cd $(BUILD_DIR); zip -r9 lambda.zip *.py -x "_temp*.*"
	cd $(BUILD_DIR); zip -r9 layer.zip python
	rm -rf $(BUILD_DIR)/python $(BUILD_DIR)/*.py

unittest-app:
	PYTHONPATH=. pytest tests/app/unit/

unittest-lambda:
	DB_USER=test DB_PASSWORD=test DB_HOST=test DB_PORT=0 DB_NAME=test PYTHONPATH=.:aws_lambda pytest -p no:warnings tests/aws_lambda/unit/

component-app:
	behave tests/app/component/features/

component-lambda:
	PYTHONPATH=.:aws_lambda behave tests/aws_lambda/component/features/

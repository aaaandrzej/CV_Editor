BUILD_DIR ?= _build

build:
	pip install sqlalchemy pymysql -t $(BUILD_DIR)/python
	cp aws_lambda/*.py $(BUILD_DIR)/
	cd $(BUILD_DIR); zip -r9 lambda.zip *.py -x "_temp*.*"
	cd $(BUILD_DIR); zip -r9 layer.zip python
	rm -rf $(BUILD_DIR)/python $(BUILD_DIR)/*.py

unittest:
	PYTHONPATH=.:aws_lambda pytest

component-app:
	behave tests/app/component/features/

component-lambda:
	PYTHONPATH=. alembic downgrade base
	PYTHONPATH=. alembic upgrade head
	PYTHONPATH=.:aws_lambda behave tests/aws_lambda/component/features/
	PYTHONPATH=. alembic downgrade base
	PYTHONPATH=. alembic upgrade head
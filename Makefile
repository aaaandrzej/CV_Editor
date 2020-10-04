build:
	pip install sqlalchemy pymysql -t _build/python
	cp aws_lambda/*.py _build/
	cd _build; zip -r9 lambda.zip *.py -x "_temp*.*"
	cd _build; zip -r9 layer.zip python
	rm -rf _build/python _build/*.py


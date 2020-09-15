FROM python:slim as python-base

FROM python-base as runtime

RUN apt-get update
RUN apt-get install -y curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

COPY poetry.lock pyproject.toml ./
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry config virtualenvs.create false
RUN poetry install

COPY app ./app
COPY features ./features
COPY tests ./tests
COPY alembic ./alembic
COPY alembic.ini ./

WORKDIR /

EXPOSE 5000

CMD PYTHONPATH=. DB_HOST=localhost DB_PORT=3306 DB_ROOT_USER=root DB_ROOT_PASSWORD=root DB_NAME=my_db python app/main.py
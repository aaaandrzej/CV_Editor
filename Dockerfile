FROM python:slim as python-base

RUN apt-get update
RUN apt-get install -y curl
RUN mkdir /app
RUN curl -o /app/get-poetry.py -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py

FROM python:slim as runtime

WORKDIR /src

COPY --from=python-base /app/get-poetry.py /src/
RUN python /src/get-poetry.py

COPY poetry.lock pyproject.toml /src/
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry config virtualenvs.create false
RUN poetry install  --no-dev
RUN rm -f /stc/get-poetry.py

COPY alembic.ini /src/
COPY alembic /src/alembic
COPY app /src/app

EXPOSE 5000

CMD PYTHONPATH=. python app/main.py
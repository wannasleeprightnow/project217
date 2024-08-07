FROM python:3.12-slim

RUN mkdir /code

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry

COPY poetry.lock pyproject.toml .

RUN poetry config virtualenvs.create false

RUN poetry install --with=dev --no-root --no-interaction --no-ansi

COPY . .

EXPOSE 8080

RUN chmod +x docker_compose/app.sh

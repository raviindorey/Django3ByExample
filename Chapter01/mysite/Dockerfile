FROM python:3.8

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000

WORKDIR /code

COPY Pipfile Pipfile.lock /code/

RUN pip install pipenv \
    && pipenv install --system \
    && rm -rf /root/.cache/pip/

COPY . .

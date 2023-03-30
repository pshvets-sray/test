FROM python:{{cookiecutter.python_version}}-buster

COPY . /app
WORKDIR /app

RUN python -m pip install -r requirements.txt --no-cache-dir

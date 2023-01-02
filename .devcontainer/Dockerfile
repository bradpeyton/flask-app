# syntax=docker/dockerfile:1
# FROM python:3.12.0a3-slim@sha256:5e2a0e6b031c68dcdc3b002de093dc2d08ab04062192df4b0968b91a3916249e
FROM mcr.microsoft.com/devcontainers/base:ubuntu
WORKDIR /flask-app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=127.0.0.1
RUN apt update
RUN apt upgrade -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip install -U pip
RUN pip install -U pycodestyle
RUN pip install -U autopep8
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
# CMD ["flask", "run"]

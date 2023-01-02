# syntax=docker/dockerfile:1
# FROM python:3.12.0a3-slim@sha256:5e2a0e6b031c68dcdc3b002de093dc2d08ab04062192df4b0968b91a3916249e
FROM mcr.microsoft.com/devcontainers/base:ubuntu
# WORKDIR .
ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0
RUN apt update
RUN apt upgrade -y
RUN apt install gcc musl-dev linux-headers -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN apt install python-dev -y
RUN pip install -U pip
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
RUN flask run
# CMD ["flask", "run"]

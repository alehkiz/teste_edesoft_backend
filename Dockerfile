# syntax=docker/dockerfile:1

FROM python:3.9.5-slim-buster

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /usr/src/app/
RUN touch /usr/src/app/logs/errors.log /usr/src/app/logs/logs.log
RUN apt-get update 
RUN apt-get -y install locales
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR:pt
ENV LC_ALL pt_BR.UTF-8

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
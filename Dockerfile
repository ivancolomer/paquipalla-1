FROM python:3.6-alpine
RUN apk update
RUN apk add build-base postgresql-dev postgresql-client
RUN mkdir /app
ADD requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
ADD . /app/

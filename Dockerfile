# syntax=docker/dockerfile:1
FROM python:3.8.2
ENV PYTHONUNBUFFERED=1
WORKDIR /project
COPY requirements.txt /project/
RUN pip install -r requirements.txt
COPY . /project/
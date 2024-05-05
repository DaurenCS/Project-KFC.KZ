FROM python:3.10.6-slim-buster as builder

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

FROM builder as runner

COPY . /project
WORKDIR /project

COPY requirements.txt /project/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /project/

EXPOSE 8000
CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000
FROM python:3.8.16-slim-bullseye

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copies the directory to the app directory
COPY ./Server ./app

# choose the default path for the container
WORKDIR /app

RUN apt-get update && \
    # these two libraries must be installed to make django work with mariadb/mysql database
    pip install pip --upgrade && \
    pip install -r requirements.txt

CMD python ./main.py

# pull official base image
FROM python:3.11.4

# set work directory
WORKDIR /usr/src/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y postgresql postgresql-contrib gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy project
COPY . .

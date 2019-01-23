FROM python:3.7.2

ENV PYTHONUNBUFFERED 1

# Creates a directory to store the project files
RUN mkdir /api
# Defines the work directory
WORKDIR /api
# "Copy" requirements.txt to directory
ADD requirements.txt /api/
# Install dependencies
RUN pip install -r requirements.txt

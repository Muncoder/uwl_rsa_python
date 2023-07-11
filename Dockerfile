FROM python:latest
RUN apt-get update
RUN pip3 install --upgrade pip
RUN pip3 install rsa
WORKDIR /app
COPY . ./

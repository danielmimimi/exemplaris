FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update
RUN apt-get -y install gcc libpq-dev

RUN pip3 install --upgrade pip
COPY . .
RUN pip3 install -r requirements.txt

CMD [ "python3", "main.py"]
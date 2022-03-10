FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install --upgrade pip
COPY . .
RUN pip3 install -r requirements.txt

CMD [ "python3", "main.py"]
FROM python:3.8-slim-buster

ENV DB_NAME="datababe"
ENV DB_USER="supaUs3r"
ENV DB_PASS="supaS3cure"
ENV TABLE_NAME="babe"

WORKDIR /app

RUN pip3 install --upgrade pip
COPY . .
RUN pip3 install -r requirements.txt

CMD [ "python3", "main.py"]
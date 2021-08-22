FROM python:3.9-slim-buster
#FROM python:3

WORKDIR /app

RUN apt-get update 
RUN apt-get install -y sudo python python3 python-pip python3-pip build-essential

COPY requirements.txt requirements.txt 

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["python3","./main.py"] 
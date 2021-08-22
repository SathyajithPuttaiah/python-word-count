FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

WORKDIR /app

COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT ["python3","./flask_app.py"]
#CMD ["flask_app_copy.py"]

FROM ubuntu:latest

WORKDIR /app

COPY . /app

RUN apt-get -y update  && apt-get install -y python
RUN pip install python-telegram-bot

CMD ["python", "main.py"]
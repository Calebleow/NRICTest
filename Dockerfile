FROM python:3.8

ADD main.py .

RUN pip install python-telegram-bot

CMD [ "python3", "main.py" ]
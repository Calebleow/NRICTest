FROM python:3

ADD main.py /

RUN pip install python-telegram-bot

CMD [ "python", "./main.py" ]
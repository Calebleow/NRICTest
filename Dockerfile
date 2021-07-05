FROM python:3.8
EXPOSE port:8080

ADD main.py .

RUN pip install python-telegram-bot

CMD [ "python3", "main.py" ]
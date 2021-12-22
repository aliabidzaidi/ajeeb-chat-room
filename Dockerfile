FROM python:2.7
COPY . /ajeeb-chat-room
WORKDIR /ajeeb-chat-room

RUN pip install -r requirements.txt
EXPOSE 5100

CMD ["python", "app.py"]

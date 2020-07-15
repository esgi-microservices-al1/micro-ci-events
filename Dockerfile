FROM python:3.7.4-alpine3.10

RUN mkdir /events && cd events && mkdir /app

WORKDIR /events

COPY app/requirements.txt /events/app/requirements.txt

RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install -r app/requirements.txt

COPY app /events/app
COPY app.py /events
COPY boot.sh /events

ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait
RUN chmod +x /events/boot.sh

EXPOSE 5000

CMD ["python", "app.py"]



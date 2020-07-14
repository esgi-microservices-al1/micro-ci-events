FROM python:3.7.4-alpine3.10

RUN mkdir /events && cd events && mkdir /app

WORKDIR /events

COPY app/requirements.txt /events/app/requirements.txt

RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install -r app/requirements.txt

COPY app /events/app
COPY app.py /events

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]



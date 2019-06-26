FROM python:3

ADD logSubscriber.py /
COPY ipadress.py /

RUN pip install paho-mqtt

CMD [ "python", "./logSubscriber.py" ]
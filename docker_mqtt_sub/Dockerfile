FROM python:3

ADD Subscriber.py /
COPY ipadress.py /

RUN pip install paho-mqtt

CMD [ "python", "./Subscriber.py" ]
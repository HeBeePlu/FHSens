FROM python:3

ADD SensorDummy.py /
COPY ipadress.py /

RUN pip install paho-mqtt

CMD [ "python", "./SensorDummy.py" ]
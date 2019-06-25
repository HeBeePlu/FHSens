FROM python:3

ADD filter.py /
COPY ipadress.py /

RUN pip install paho-mqtt

CMD [ "python", "./filter.py" ]
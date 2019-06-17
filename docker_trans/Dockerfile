FROM python:3

ADD transformer.py /
COPY ipadress.py /

RUN pip install paho-mqtt

CMD [ "python", "./transformer.py" ]
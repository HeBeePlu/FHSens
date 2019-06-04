FROM python:3



ENV UDPPORT 8888 
ADD udp2mqtt.py /
COPY ipadress.py /


RUN pip install paho-mqtt \
  && pip install virtualenv

CMD [ "python", "./udp2mqtt.py" ]

EXPOSE ${UDPPORT}
EXPOSE ${UDPPORT}/udp
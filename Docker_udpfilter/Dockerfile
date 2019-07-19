FROM python:3



ENV UDPPORT 8888 
ADD udpfilter.py /
COPY ipadress.py /


RUN pip install paho-mqtt \
  && pip install virtualenv

CMD [ "python", "./udpfilter.py" ]

EXPOSE ${UDPPORT}
EXPOSE ${UDPPORT}/udp
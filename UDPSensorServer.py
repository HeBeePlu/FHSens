# UDP server zur annahme der sensordten

import socket
import time
import numpy
import paho.mqtt.client as mqtt

#UDP Socket Setup
UDP_IP_ADDRESS = "192.168.178.45" # IP vom Server (Empfänger-Standpunkt)
UDP_PORT_NO = 49200

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
print ('UDP Server up: Port 49200')

#MQTT Publisher Setup
broker_adress = "192.168.178.45"

sensorClient = mqtt.Client()
sensorClient.connect(broker_adress)
sensorClient.loop_start()

while True:
    data, addr = serverSock.recvfrom(1024)
    sensorClient.publish("Sensor", data)
    
    print("Message: ", data)
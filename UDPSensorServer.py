# UDP server zur annahme der sensordten und weitergabe an MQTT Brocker in Form eines JSON Paketes

import socket
import time
import numpy
import paho.mqtt.client as mqtt
import json
import ipadress

#UDP Socket Setup
UDP_IP_ADDRESS = "192.168.178.45" # IP vom Server (Empfanger-Standpunkt)
UDP_PORT_NO = 49200

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
print ('UDP Server up: Port 49800')

#MQTT Publisher Setup
broker_adress = "192.168.178.45"

sensorClient = mqtt.Client()
sensorClient.connect(broker_adress)
sensorClient.loop_start()

print('MQTT Client up')
print ('UDP-to-MQTT-Service IP: ', ipadress.get_ip())
while True:
    data, addr = serverSock.recvfrom(1024)
    dataToMQTT = json.dumps(data)
    sensorClient.publish("Sensor", dataToMQTT)
    
    print("Message: ", data)
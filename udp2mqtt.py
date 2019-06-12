# UDP server zur annahme der sensordten und weitergabe an MQTT Brocker in Form eines JSON Paketes

import socket
from datetime import datetime
import numpy
import paho.mqtt.client as mqtt
import json
import ipadress

#UDP Socket Setup
UDP_IP_ADDRESS = "192.168.178.45" # IP vom Server (Empfanger-Standpunkt)
UDP_PORT_NO = 8888

service_ip = ipadress.get_ip()
service_name = 'UDPtoMQTT Service'
service_status = True

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
print ('UDP Server up: ' + str(UDP_PORT_NO))

#MQTT Publisher Setup
broker_adress = "192.168.178.45"


serviceClient = mqtt.Client()
serviceClient.connect(broker_adress)
serviceClient.loop_start()
print('MQTT Client up')


print ('UDPtoMQTT_Service IP: ', service_ip)

def main ():
    while True:
        data, addr = serverSock.recvfrom(1024)
        timeStamp = str(datetime.now().time())
        msg = {'Messwert': data, 'Zeit udp2mqtt' : timeStamp}
        dataToMQTT = json.dumps(msg)
        #serviceClient.publish("UDP-Sensor", data)
        serviceClient.publish("UDP-Sensor", dataToMQTT)
        print("Message: ", dataToMQTT)
            
if __name__=='__main__':
    main()        
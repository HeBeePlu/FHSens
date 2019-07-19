# UDP server zur annahme der sensordten und weitergabe an MQTT Brocker in Form eines JSON Paketes

import socket
from datetime import datetime
import paho.mqtt.client as mqtt
import json
import ipadress
import os

#UDP Socket Setup
ip = ipadress.get_ip() #ermittelt die IP Adresse des Containers
UDP_IP_ADDRESS = str(ip) # IP vom Server (Empfanger-Standpunkt)
UDP_PORT_NO = int(os.environ['UDPPORT'])
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP Socket erstellen

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
print ('UDP Server up: ' + str(UDP_PORT_NO))

#MQTT Publisher Setup
broker_adress = "192.168.178.45"


serviceClient = mqtt.Client()
serviceClient.connect(broker_adress)
serviceClient.loop_start()
print('MQTT Client up')


print ('UDPtoMQTT_Service IP: ', str(ip))

def zeitformat (zeit):
    zeitList = list()
    for n in range(6, 14):
        zeitList.append(zeit[n])
    zeitString = ''.join(str(i) for i in zeitList)
    return zeitString 

trigger = 0

def main ():
    global trigger
    while True:
        data, addr = serverSock.recvfrom(1024)
        data = str(data)
        n = (len(data))
        if(trigger != n):
            timeStamp = str(datetime.now().time())
            timeStamp = zeitformat(timeStamp)
            msg = {'Messwert': data, 'Zeit udp2mqtt' : timeStamp}
            dataToMQTT = json.dumps(msg)
            serviceClient.publish("UDP-Sensor/Filter", dataToMQTT)
            print("Message: ", dataToMQTT)
            trigger = n #setzen der ausloeservariable auf vorher gueltigen wert
            
if __name__=='__main__':
    main()        
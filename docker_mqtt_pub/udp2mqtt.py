# UDP server zur annahme der sensordten und weitergabe an MQTT Brocker in Form eines JSON Paketes
#
#zum starten des Containers via Docker: docker run -d --name 'Containername' 'Image'
#
#Hendrik Beecken
#

import socket
import os
import paho.mqtt.client as mqtt
import json
import ipadress
from datetime import datetime

#UDP Socket Setup
ip = ipadress.get_ip() #ermittelt die IP Adresse des Containers
UDP_IP_ADDRESS = str(ip) # IP vom Server (Empfanger-Standpunkt)
UDP_PORT_NO = int(os.environ['UDPPORT'])
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP Socket erstellen

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))


#MQTT Publisher Setup
broker_adress = "192.168.178.45" #IP Adresse des MQTT Brokers

serviceClient = mqtt.Client()
serviceClient.connect(broker_adress)
serviceClient.loop_start()
print('MQTT Client up ' + str(ip))

adress = str(ip)
adressToMQTT=json.dumps(adress)
serviceClient.publish("UDP-Sensor", adressToMQTT) #testweise senden der Container IP uber mqtt

def zeitformat (zeit):
    zeitList = list()
    for n in range(6, 14):
        zeitList.append(zeit[n])
    zeitString = ''.join(str(i) for i in zeitList)
    return zeitString 

def main ():
    try:
        while True:
            data, addr = serverSock.recvfrom(1024) #Daten vom UDP Port empfangen
            timeStamp = str(datetime.now().time())
            aufnahmeZeit = zeitformat(timeStamp)
            aufnahmeZeit = str(aufnahmeZeit)
            data = str(data)
            msg = {'Messwert': data, 'Zeit udp2mqtt' : aufnahmeZeit}
            dataToMQTT = json.dumps(msg)
            serviceClient.publish("UDP-Sensor", dataToMQTT) #Daten im JSON Format an MQTT Topic senden
            print("Message: ", dataToMQTT)
            
            
    except:
        print('Konvertierung fehlgeschlagen')
        
if __name__=='__main__':
    main()        
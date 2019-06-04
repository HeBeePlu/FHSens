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

def main ():
    
    while True:
        data, addr = serverSock.recvfrom(1024) #Daten vom UDP Port empfangen
        #dataToMQTT = json.dumps(data)
        serviceClient.publish("UDP-Sensor", data) #Daten an MQTT Topic senden
        
        print("Message: ", data, adress)
            
if __name__=='__main__':
    main()        
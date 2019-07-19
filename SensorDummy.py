# Dieses Srcipt simuliert einen Sensor, der Daten an via UDP ubertraegt
# Dies ist ein UDP Client, welcher Beispiel-Daten an den UDP Server sendet
#
#
#
#
# Hendrik Beecken


import socket
import time
import ipadress
import json
import paho.mqtt.client as mqtt

#UDP_IP_ADDRESS = "192.168.178.45" #IP des RasPI zum testen ausserhalb des containers
UDP_IP_ADDRESS = "172.17.0.2" #IP des UDP2MQTT uebersetzers
#UDP_IP_ADDRESS = "172.17.0.4" #IP des UDP Filter containers
UDP_PORT_NO = 8888

#MQTT Publisher Setup
broker_adress = "192.168.178.45"

sensorClient = mqtt.Client()
sensorClient.connect(broker_adress)
sensorClient.loop_start()

print('MQTT Client up')

service_ip = ipadress.get_ip()

sleepTime = 0.02 # daten im 12ms Takt

#erstellen eines Sockets zur Verbindung mit dem Server
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('UDP Sensor socket up')
print('sende Daten an: ' + UDP_IP_ADDRESS)
    
def main():
    try:
        while True:
            for msg in range(0, 256):
                msg=str(msg)
                clientSock.sendto(msg.encode('utf-8'), (UDP_IP_ADDRESS, UDP_PORT_NO))
                #time.sleep(sleepTime)
                
            for msg in range (256, 0, -1):
                msg=str(msg)
                clientSock.sendto(msg.encode('utf-8'), (UDP_IP_ADDRESS, UDP_PORT_NO))
                #time.sleep(sleepTime)
    except:
        
        print("Sensor down")

if __name__=='__main__':
    main()
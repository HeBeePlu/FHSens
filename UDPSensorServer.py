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

service_ip = ipadress.get_ip()
service_name = 'UDPtoMQTT Service'
service_status = True

service_props = { 'ServiceName' : service_name,
                  'Service IP' : service_ip,
                  'Servicestatus' : service_status }

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
print ('UDP Server up: ' + str(UDP_PORT_NO))

#MQTT Publisher Setup
broker_adress = "192.168.178.45"

sensorClient = mqtt.Client()
sensorClient.connect(broker_adress)
sensorClient.loop_start()
print('MQTT Client up')

register_msg = json.dumps(service_props)
sensorClient.publish("ServiceRegister", register_msg)
print ('UDPtoMQTT_Service IP: ', service_ip)

def main ():
    try:
        while True:
            data, addr = serverSock.recvfrom(1024)
            dataToMQTT = json.dumps(data)
            sensorClient.publish("UDP-Sensor", dataToMQTT)
            
            print("Message: ", data)
    except:
            service_status = False
            service_props.update({'Servicestatus': service_status})
            register_msg = json.dumps(service_props)
            sensorClient.publish("ServiceRegister", register_msg)
            print("UDPtoMQTT Service down")
            
    
if __name__=='__main__':
    main()
# Dieses Skript soll ein Dummy fur einen Sensor sein, welcher seine Messdaten uber UDP versendet
# Dies ist ein UDP Client, welcher Daten an den UDP Server senden soll

import socket
import time
import ipadress

UDP_IP_ADDRESS = "192.168.178.45"
UDP_PORT_NO = 49200

service_ip = ipadress.get_ip()
service_name = 'Sensor Dummy'
service_status = True

sleepTime = 0.012

#erstellen eines Sockets zur Verbindung mit dem Server
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('UDP Sensor socket up')

service_props = { 'ServiceName' : service_name,
                  'Service IP' : service_ip,
                  'Servicestatus' : service_status }
    

register_msg = json.dumps(service_props)
sensorClient.publish("ServiceRegister", service_props)
print ('UDP-Sensor IP: ', service_ip)
#senden der Daten an den server
def main():
    try:
        while service_status = True:
            for msg in range(0, 256):
                msg=str(msg)
                clientSock.sendto(msg.encode('utf-8'), (UDP_IP_ADDRESS, UDP_PORT_NO))
                time.sleep(sleepTime)
                
            for msg in range (256, 0, -1):
                msg=str(msg)
                clientSock.sendto(msg.encode('utf-8'), (UDP_IP_ADDRESS, UDP_PORT_NO))
                time.sleep(sleepTime)
    except:
        service_status = False
        service_props.update({'Servicestatus': service_status})
        register_msg = json.dumps(service_props)
        sensorClient.publish("ServiceRegister", service_props)
        print("Sensor abgestürzt")

if __name__=='__main__':
    main()
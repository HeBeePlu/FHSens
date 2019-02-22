# Dieses Skript soll ein Dummy für einen Sensor sein, welcher seine Messdaten über UDP versendet
# Dies ist ein UDP Client, welcher Daten an den UDP Server senden soll

import socket
import time

UDP_IP_ADDRESS = "192.168.178.45"
UDP_PORT_NO = 49200

msg = "Hallo Server"
sleepTime = 0.012

#erstellen eines Sockets zur Verbindung mit dem Server
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('UDP socket up')
#senden der Daten an den server
def main():
    while True:
        for msg in range(0, 256):
            msg=str(msg)
            clientSock.sendto(msg.encode('utf-8'), (UDP_IP_ADDRESS, UDP_PORT_NO))
            time.sleep(sleepTime)
            
        for msg in range (256, 0, -1):
            msg=str(msg)
            clientSock.sendto(msg.encode('utf-8'), (UDP_IP_ADDRESS, UDP_PORT_NO))
            time.sleep(sleepTime)

if __name__=='__main__':
    main()
# Dieses Skript soll ein Dummy für einen Sensor sein, welcher seine Messdaten über UDP versendet
# Dies ist ein UDP Client, welcher Daten an den UDP Server senden soll

import socket

UDP_IP_ADDRESS = "192.168.178.45
UDP_PORT_NO = 49200

msg = "Hallo Server"

#erstellen eines Sockets zur Verbindung mit dem Server
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#senden der Daten an den server
clientSock.sendto(msg, (UDP_IP_ADDRESS, UDP_PORT_NO))
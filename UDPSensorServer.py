# UDP server zur annahme der sensordten

import socket

UDP_IP_ADDRESS = "192.168.178.45"
UDP_PORT_NO = 49200

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
print ('UDP Server up: Port 49200')

while True:
    data, addr = serverSock.recvfrom(1024)
    print("Message: ", data)
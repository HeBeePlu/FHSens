# Hendrik Beecken
# 07.01.2019
#
# MQTT Publisher zur Kommunikation der Sensordaten

import time
import numpy
import paho.mqtt.client as mqtt

broker_adress = "192.168.178.45"

client = mqtt.Client() #mqtt.Client("Client_Name") optional aber Name darf nur ein mal vergeben werden

#client.connect("localhost", 1883, 60)
client.connect(broker_adress)

client.loop_start()


#publish Data zum Topic 'topic'
def dauerschleife(string):
    while True:
        client.publish("topic",string)
        time.sleep(1)


def koordinaten_eingabe():
    koordinatenliste = numpy.empty(3, dtype=float)
    
    koordinatenliste [0] = input("X-Koordinate: ")
    koordinatenliste [1] = input("Y-Koordinate: ")
    koordinatenliste [2] = input("Z-Koordinate: ")
    
    return koordinatenliste

def create_string(eingabeliste):
    eingabeliste = list(map(lambda x: str(x), eingabeliste))
    
    return 'X: ' + eingabeliste[0] + ' Y: ' + eingabeliste[1] + ' Z: ' + eingabeliste[2]

if __name__=='__main__':
    dauerschleife(create_string(koordinaten_eingabe()))
    #koordinaten_eingabe()


# Hendrik Beecken
# 07.01.2019
#
# MQTT Publisher zur Kommunikation der Sensordaten

import time
import paho.mqtt.client as mqtt

broker_adress = "192.168.178.45"

client = mqtt.Client() #mqtt.Client("Client_Name") optional aber Name darf nur ein mal vergeben werden

#client.connect("localhost", 1883, 60)
client.connect(broker_adress)

client.loop_start()


#publish Data zum Topic 'topic'
def dauerschleife():
    while True:
        client.publish("topic","Py Script Hallo")
        time.sleep(1)

if __name__=='__main__':
    dauerschleife()



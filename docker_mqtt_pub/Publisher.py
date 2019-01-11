# Hendrik Beecken
# 07.01.2019
#
# MQTT Publisher zur Kommunikation der Sensordaten

import time
import paho.mqtt.client as mqtt

broker_adress = "192.168.178.45"

client = mqtt.Client()

#client.connect("localhost", 1883, 60)
client.connect(broker_adress)

client.loop_start()


#publish Data zum Topic 'topic'
while True:
    client.publish("topic","Hallo von Docker")
    time.sleep(2)





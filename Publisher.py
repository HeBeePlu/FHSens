# Hendrik Beecken
# 07.01.2019
#
# MQTT Broker zur Kommunikation der Sensordaten


import paho.mqtt.client as mqtt

broker_adress = "192.168.178.45"

client = mqtt.Client("Publisher_1")

#client.connect("localhost", 1883, 60)
client.connect(broker_adress)

#publish Data
client.publish("fun/topic","Py Script Hallo")

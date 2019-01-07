# Hendrik Beecken
# 07.01.2019
#
# MQTT Broker zur Kommunikation der Sensordaten

import os
import paho.mqtt.client as mqtt

#broker_adress = "192.168.178.45"

# Startet mosquitto Broker auf Port 1883 im Hintergrund
os.system('mosquitto -p 1883 -d')
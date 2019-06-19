# Datenverarbeitung als Filter
# 
# nimmt eingehende Daten an und gibt jede 10te eingehende nachricht auf neuem Topic weiter
#
#

import paho.mqtt.client as mqtt
import json
#import yaml
import ipadress
from datetime import datetime

broker_adress = "192.168.178.45" #ip des geraetes, auf dem der mqtt brocker laeuft

client = mqtt.Client()#mqtt.Client("Client_Name") optional aber Name darf nur ein mal vergeben werden

#client.connect("localhost", 1883, 60) #alternative zur ip
client.connect(broker_adress)


#Topic "udp-sensor" wird abonniert mit einem Quality of Service qos
client.subscribe("UDP-Sensor", 0)
print('MQTT Client up')

#Infos dieses Services
service_ip = ipadress.get_ip()
service_name = 'Filter Service'
print ('Subscriber_Service IP: ', service_ip)

#funktion zum auslesen des mqtt topics 'UDP-Sensor' und weiterleiten an neues Topic 'data-filter'
def on_message(client, userdata, msg):
    #msg_in = msg.payload
    msg_in = json.loads(msg.payload) #json daten entpacken
    #msg_in = msg_in.encode('latin1')
    #timeStamp = str(datetime.now().time()) #zeitstempel einfuegen
    #newMsg = str(msg_in) + ' ' + timeStamp #neue Message an ein weiteres MQTT Topic erstellen
    #dataFiltered = json.dumps(newMsg) #als JSON verpacken
    #print(newMsg)
    #client.publish("UDP-Sensor/Filter", dataFiltered) # an das Topic 'Data-Log' senden
    #print('Log Subscriber: ' + newMsg)
    print (msg_in['Messwert'])
    
def main():
    try:
        
        client.on_message = on_message
        client.loop_forever()
    # stoerungsmeldung 
    except:
        
        print("Subscriber Service down")

if __name__=='__main__':
    main()
# Datenverarbeitung als Filter
# 
# nimmt eingehende Daten an und gibt jede 10te eingehende nachricht auf neuem Topic weiter
#
#

import paho.mqtt.client as mqtt
import json
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
    
    msg_in = json.loads(msg.payload) #json daten entpacken
    data = msg_in['Messwert'] #messwert extrahieren
    #data = data.encode('ascii', 'ignore') # von unicode zu string wandeln
    print (len(data))
    if len(data) == 5:
        data = data[2] + data[3] #wert als ziffern isolieren
        data = int(data) #string zu int wandeln
        
    else:
        data = data[2] + data [3] + data [4]
        data = int(data)
    # Filter zum auswahlen bestimmter werte      
    if data == 11 or data == 12 : #bestimmte werte sollen versendet werden
        timeStamp = str(datetime.now().time()) #zeitstempel einfuegen
        newMsg = str(msg_in) + ' ' + str(data) + ' ' + timeStamp #neue Message an ein weiteres MQTT Topic erstellen
        newMsg = str(newMsg)
        dataFiltered = json.dumps(newMsg) #als JSON verpacken
        client.publish("UDP-Sensor/Filter", dataFiltered) # an das Topic senden
        print (newMsg)
    else:
        print(msg_in['Messwert'])
    
def main():
    try:        
        client.on_message = on_message
        client.loop_forever()
    # stoerungsmeldung 
    except:
        
        print("Filter Service down")

if __name__=='__main__':
    main()
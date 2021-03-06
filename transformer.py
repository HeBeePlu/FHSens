# Datenverarbeitung als Durchgangststion zwischen diversen Containern
#
# nimmt eingehende Daten an und gibt sie auf anderem topic wieder aus
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
service_name = 'Durchgangs Service'
print ('Subscriber_Service IP: ', service_ip)

#funktion zum auslesen des mqtt topics 'UDP-Sensor' und weiterleiten an neues Topic 'Data-Log'
def on_message(client, userdata, msg):
    msg_in = json.loads(msg.payload) #json daten entpacken
    timeStamp = str(datetime.now().time()) #zeitstempel einfuegen
    msg_in.update({'Topic Change' : timeStamp}) #neue Message an ein weiteres MQTT Topic erstellen
    dataToMQTT = json.dumps(msg_in) #als JSON verpacken
    #print(newMsg)
    client.publish("Data-Log", dataToMQTT) # an das Topic 'Data-Log' senden
    print(msg_in)
    
def main():
    try:
        #client.loop_start()
        client.on_message = on_message
        client.loop_forever()
    # stoerungsmeldung 
    except:
        
        print("Subscriber Service down")

if __name__=='__main__':
    main()
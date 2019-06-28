#Hendrik Beecken
#
#07.01.2019
#
#Subscriber-Script



import paho.mqtt.client as mqtt
import json
import ipadress
from datetime import datetime
from datetime import timedelta

broker_adress = "192.168.178.45" #ip des geraetes, auf dem der mqtt brocker laeuft

client = mqtt.Client()#mqtt.Client("Client_Name") optional aber Name darf nur ein mal vergeben werden

#client.connect("localhost", 1883, 60) #alternative zur ip
client.connect(broker_adress)

#alle topics ab UDP-Sensor/ werden abonniert mit einem Quality of Service qos
client.subscribe("UDP-Sensor/#", 0)
#client.subscribe("Data-Log", 0)
print('MQTT Client up')

service_ip = ipadress.get_ip()
service_name = 'Subscriber Service'

print ('Subscriber_Service IP: ', service_ip)

def zeitformat (zeit):
    zeitList = list()
    for n in range(6, 14):
        zeitList.append(zeit[n])
    zeitString = ''.join(str(i) for i in zeitList)
    return zeitString        
            
#funktion zum auslesen des mqtt topics
def on_message(client, userdata, msg):
    msg_in = json.loads(msg.payload) #json daten entpacken
    timeStamp = str(datetime.now().time()) #zeitstempel einfuegen
    msg_in.update({'Subscriber Zeit' : timeStamp})
    starttime = str(msg_in['Zeit udp2mqtt'])
    
    a = zeitformat(msg_in['Zeit udp2mqtt'])
    
    print(a)
    
def main():
    try:
        client.on_message = on_message
        client.loop_forever()
    # stoerungsmeldung 
    except:
        
        print("Subscriber Service down")

if __name__=='__main__':
    main()
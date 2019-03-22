
#Register und Monitoring Service
# 19.03.2019

import paho.mqtt.client as mqtt
import json
import ipadress
from pymongo import MongoClient

#Initialisieren der datenbank zum Servicemonitoring
dataClient = MongoClient(port = 27017)
db = dataClient.serviceMonitor

#MQTT Client einrichten
broker_adress = "192.168.178.45"
client = mqtt.Client()#mqtt.Client("Client_Name") optional aber Name darf nur ein mal vergeben werden
#client.connect("localhost", 1883, 60) #alternative zur ip
client.connect(broker_adress)
#Topic "topic" wird abonniert mit einem Quality of Service qos
client.subscribe("ServiceRegister", 0)
print('MQTT Client up')

service_ip = ipadress.get_ip()
service_name = 'Monitoring Service'
service_status = True

service_props = { service_name : {
                  'Service IP' : service_ip,
                  'Servicestatus' : service_status }}

register_msg = json.dumps(service_props)
client.publish("ServiceRegister", register_msg)
print ('Monitoring_Service IP: ', service_ip)



def on_message(client, userdata, msg):
    serviceToMonitor = json.loads(msg.payload)
    
    print(str(serviceToMonitor))
    
    
def main():
    try:
        client.on_message = on_message
        client.loop_forever()
        
    except:
        service_status = False
        service_props[service_name]['Servicestatus'] = service_status
        register_msg = json.dumps(service_props)
        client.publish("ServiceRegister", register_msg)
        print("Monitoring Service down")

if __name__=='__main__':
    main()
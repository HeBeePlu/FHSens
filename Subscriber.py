#Hendrik Beecken
#
#07.01.2019
#
#Subscriber-Script



import paho.mqtt.client as mqtt
import json
import ipadress

broker_adress = "192.168.178.45"

client = mqtt.Client()#mqtt.Client("Client_Name") optional aber Name darf nur ein mal vergeben werden

#client.connect("localhost", 1883, 60) #alternative zur ip
client.connect(broker_adress)

#Topic "topic" wird abonniert mit einem Quality of Service qos
client.subscribe("UDP-Sensor", 0)
print('MQTT Client up')

service_ip = ipadress.get_ip()
service_name = 'Subscriber Service'
service_status = True

service_props = { 'ServiceName' : service_name,
                  'Service IP' : service_ip,
                  'Servicestatus' : service_status }

register_msg = json.dumps(service_props)
sensorClient.publish("ServiceRegister", register_msg)
print ('UDPtoMQTT_Service IP: ', service_ip)

def on_message(client, userdata, msg):
    msg_in = json.loads(msg.payload)
    print(msg.topic + " " + str(msg_in))
    
def main():
    try:
        client.on_message = on_message
        client.loop_forever()
        
    except:
        service_status = False
        service_props.update({'Servicestatus': service_status})
        register_msg = json.dumps(service_props)
        sensorClient.publish("ServiceRegister", register_msg)
        print("Subscriber Service down")

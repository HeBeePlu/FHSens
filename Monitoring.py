
#Register und Monitoring Service
# 19.03.2019

import paho.mqtt.client as mqtt
import json
import ipadress

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
    msg_in = json.loads(msg.payload)
    
    #todo monitoring dict erstellen, welches sich bei statusanderung updatet
    print(str(msg_in))
    #name = msg_in[service_name]
    ip = msg_in[1]['Service IP']
    #status = msg_in['Servicestatus']
    print(str(msg_in[0][ip]))
    
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
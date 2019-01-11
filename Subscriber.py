#Hendrik Beecken
#
#07.01.2019
#
#Subscriber-Script



import paho.mqtt.client as mqtt

broker_adress = "192.168.178.45"

client = mqtt.Client()#mqtt.Client("Client_Name") optional aber Name darf nur ein mal vergeben werden

#client.connect("localhost", 1883, 60) #alternative zur ip
client.connect(broker_adress)

#Topic "topic" wird abonniert mit einem Quality of Service qos
client.subscribe("topic", 0)

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    
    
client.on_message = on_message

client.loop_forever()
import os
import paho.mqtt.client as mqtt
import json


def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    client.subscribe("home/ceilingfan")  # Subscribe to the topic, receive any messages published on it


def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
    print("message received " ,str(msg.payload.decode("utf-8")))
    print("message topic=",msg.topic)
    print("message qos=",msg.qos)
    print("message retain flag=",msg.retain)
    jdict = json.loads(str(msg.payload.decode("utf-8")))
    print(jdict)
    if ('light' in jdict):
        if (jdict['light'] == "toggle"):
            os.system('./sendiq -s 250000 -f 304.765e6 -t u8 -i r_light.iq')
    elif ('fan' in jdict):
        if (jdict['fan'] == "direction"):
            os.system('./sendiq -s 250000 -f 304.765e6 -t u8 -i r_direction.iq')
        if (jdict['fan'] == "stop" or jdict['fan'] == "0"):
            os.system('./sendiq -s 250000 -f 304.765e6 -t u8 -i r_stop.iq')
        if (jdict['fan'] == "1"):
            os.system('./sendiq -s 250000 -f 304.765e6 -t u8 -i r_level_L.iq')
        if (jdict['fan'] == "2"):
            os.system('./sendiq -s 250000 -f 304.765e6 -t u8 -i r_level_II.iq')
        if (jdict['fan'] == "3"):
            os.system('./sendiq -s 250000 -f 304.765e6 -t u8 -i r_level_III.iq')
        if (jdict['fan'] == "4"):
            os.system('./sendiq -s 250000 -f 304.765e6 -t u8 -i r_level_IV.iq')
        if (jdict['fan'] == "5"):
            os.system('./sendiq -s 250000 -f 304.765e6 -t u8 -i r_level_V.iq')
        if (jdict['fan'] == "6"):
            os.system('./sendiq -s 250000 -f 304.765e6 -t u8 -i r_level_H.iq')
        print(jdict)

broker_address="mqttbroker"
broker_port=1883

client = mqtt.Client("fan_controller")  # Create instance of client with client ID “digi_mqtt_test”
client.on_connect = on_connect  # Define callback function for successful connection
client.on_message = on_message  # Define callback function for receipt of a message
client.connect(broker_address, broker_port)
client.loop_forever()  # Start networking daemon


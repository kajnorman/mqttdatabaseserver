import paho.mqtt.client as mqtt
import sqlite3
dbFile =  "data/data.db"



def writeToDb(Key, Value):
    conn = sqlite3.connect(dbFile)
    c = conn.cursor()
    print( "Writing to db...")
    c.execute("INSERT INTO full_table (reading_time ,key ,value) VALUES (DATETIME('now'),?,?)", (Key, Value))
    conn.commit()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("trek/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    writeToDb(msg.topic , str(msg.payload))



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()

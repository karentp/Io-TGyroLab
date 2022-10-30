"""
El codigo realizado fue a base de la informacion obtenida de la pagina : http://www.steves-internet-guide.com/thingsboard-mqtt-dashboard/
Para comunicacion por MQTT para dashboard, en este caso ThingsBoard
"""

#Librerias

import serial
import paho.mqtt.client as mqtt
import time,json
import time

#Variable global
count=0

#FUNCIONES

def on_log(client, userdata, level, buf):
   print(buf) 

#Funcion on_connect verifica el estado de conexion si esta pudo ser realizada correctamente
# de no ser asi detiene la conexion.

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag=True 
        print("conexion OK") 

    else:

        print("La conexion no fue realizada correctamente",rc) 
        client.loop_stop()  

#Funcion de desconexion del ciente, imprime si fue realizada correctamente

def on_disconnect(client, userdata, rc): 
   print("Desconexión de cliente realizada correctamente") 


def on_publish(client, userdata, mid):
    print("In on_pub callback mid= "  ,mid)

#TECNOLOGIA MQTT

#Revision si se realizada la conexion de cliente por tec MQTT correctamente

mqtt.Client.connected_flag=False 

mqtt.Client.suppress_puback_flag=False

#Creacion de instancia 

client = mqtt.Client("python1")              

#Conexion 

client.on_connect = on_connect 

#Desconexion

client.on_disconnect = on_disconnect 

#Publicacion

client.on_publish = on_publish 

#Broker de la escuela de electrica

broker="iot.eie.ucr.ac.cr"

#Puerto

port =1883

#Topic

topic="v1/devices/me/telemetry"

#Token de usuario donde se establece la conexion

usuario="H0BEo1567kp50xpIkme9"
password=""



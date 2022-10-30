"""
El presente codigo corresponde a la comunicacion serial para visualizar  la información proveniente de la lectura de datos del giroscopio
del Discovery Kit.

La fuente de información corresponde a https://www.pythontutorial.net/python-basics/python-write-csv-file/

"""

import time, csv, serial

#Comunicacion con la placa mediante el puerto ttyACM0
lectura_serial = serial.Serial(port = '/dev/ttyACM0', baudrate = 15200,timeout=1)

filename= open("Datos.csv",'w') 
escritura_archivo = csv.writer(filename)

while (True):
	datos_escribir = lectura_serial.readline().decode().split(' ')
	escritura_archivo.writerow(datos_escribir)





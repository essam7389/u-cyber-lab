import http.client
import json
import time
import os
from random import randint
import numpy


ruta_diccionario_kali = "/root/Documents/Diccionarios/servidores_hosts.json"
print("He entrado en el archivo")
rand_exp = numpy.random.exponential(scale=10)

with open(ruta_diccionario_kali, 'r') as f:  # Se realiza la lectura del fichero JSON
    servidores = json.load(f)

#Habría que controlar que no se envían los usernames ni las contraseñas ni las ips de gestion a los hosts.
for servidor in servidores.get("hosts"):
    ip = servidor.get("nics")['data']['IP']

    conn = http.client.HTTPConnection(ip+":8000")
    conn.request("GET", "/")
    r1 = conn.getresponse()
    print(r1.status, r1.reason)

    data1 = r1.read()  # This will return entire content.
    # The following example demonstrates reading data in chunks.
    conn.request("GET", "/")
    r1 = conn.getresponse()

   # while chunk := r1.read(200):
       # print(repr(chunk))

    conn.close()

    time.sleep(rand_exp)  # Esperamos x segundos para volver a realizar otra petición de manera aleatoria con distribución exponencial de media = 5 sg

    tm = time.time()
    tiempo_inicial = time.localtime(tm)

    if(time == 0):
        tiempo_final = time.localtime(tm+60) #Pasar el parámetro de tiempo desde el manager
    else:
        tiempo = 60
        tiempo_final = time.localtime(tm+60)
    size = len(servidores)
    print("El tamaño = ", size)

    while(True):
        tiempo_inicial = time.localtime(tm)
        #Se obtiene un valor para el índice aleatorio:
        i = randint(0, size-1)
        print( "i = ", i)
        ip = servidores.get("hosts")[i].get("nics")['data']['IP']

        conn = http.client.HTTPConnection(ip + ":8000")
        conn.request("GET", "/programa")
        r1 = conn.getresponse()
        print(r1.status, r1.reason)

        data1 = r1.read()  # This will return entire content.
        # The following example demonstrates reading data in chunks.
        conn.request("GET", "/")
        r1 = conn.getresponse()

       # while chunk := r1.read(200):
           # print(repr(chunk))

        conn.close()
        time.sleep(5.00)  # Esperamos 5 segundos para volver a realizar otra petición

        ip = servidores.get("hosts")[i].get("nics")['data']['IP']

        conn = http.client.HTTPConnection(ip + ":8000")
        conn.request("GET", "/localizacion")
        r1 = conn.getresponse()
        print(r1.status, r1.reason)

        data1 = r1.read()  # This will return entire content.
        # The following example demonstrates reading data in chunks.
        conn.request("GET", "/")
        r1 = conn.getresponse()

        #while chunk := r1.read(200):
          #  print(repr(chunk))

        conn.close()

#Aleatorización:

#quien nos vamos a conectar

#a quien se lo vamos a pedir

#tiempo entre peticiones



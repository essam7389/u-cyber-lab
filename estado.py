import json
import os
import subprocess

def estado(list):
    print("Ha continuación se mostrarán las conexiones activas entre este ordenador y el resto de dispositivos.")
    with open('dispositivos.json', 'r') as f:
        direcciones_dict = json.load(f)

    cont_gestion = 0
    cont_datos = 0
    response_gestion = []
    response_datos = []


    while(cont_gestion<len(list)):

        i = list[cont_gestion]
        ip_gestion = direcciones_dict.get("devices")[i-1].get("nics")['management']
        p = subprocess.Popen(['ping', '-n', '2', '-w', '2', ip_gestion])
        p.wait()
        if p.poll() == 0:
            response_gestion.append(0)
        else:
            response_gestion.append(1)
        #gestion = os.system("ping -n 2 " + direcciones)


        print("La respuesta es:")

        cont_gestion = cont_gestion + 1

    while(cont_datos<len(list)):
        i = list[cont_datos]
        if(i != 2):
            ip_datos = direcciones_dict.get("devices")[i - 1].get("nics")['datos']['IP']
            p = subprocess.Popen(['ping', '-n', '2', '-w', '2', ip_datos])
            p.wait()
            if p.poll() == 0:
                response_datos.append(0)
            else:
                response_datos.append(1)

        cont_datos = cont_datos + 1

    print("############################################################################################ \n")

    print("Las direcciones de la RED DE GESTIÓN disponibles son: ")

    print("")

    cont = 0;
    for x in response_gestion:

        if(x == 0):
            print(direcciones_dict.get("names-gestion")[cont] + " -------------> ACTIVO" )
        else:
            print(direcciones_dict.get("names-gestion")[cont] + " -------------> INACTIVO" )

        cont += 1

    print("")

    print("---------------------------------------------------------------------------------------------")

    print("")
    print("Las direcciones de la RED DE DATOS disponibles son:")

    print(" ")
    cont = 0
    for y in response_datos:
        if (y == 0):
            print(direcciones_dict.get("names-datos")[cont] + " -------------> ACTIVO")
        else:
            print(direcciones_dict.get("names-datos")[cont] + " -------------> INACTIVO")

        cont += 1

    print("")
    print("############################################################################################ \n")


   # print(response[cont])

"""     

{
  "name": "Direcciones",
  "version": "1.0.0",
  "dispositivos": {

    "Gestion": "192.168.2.1",
    "Wifi-Router": "192.168.2.2",
    "Router1-Gestion": "192.168.2.3",
    "Router2-Gestion": "192.168.2.4",
    "Datos": "172.16.1.1",
    "Router1-Datos": "172.16.1.2",
    "Router2-Datos": "172.16.1.2.3",
    "Red-Pi1": "33.1.1.1",
    "Red-Pi2":"33.1.2.1"

  },



}
        
        
        """
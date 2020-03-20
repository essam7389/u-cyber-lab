import json
import os

def estado(ssh):
    print("Ha continuación se mostrarán las conexiones activas entre este ordenador y el resto de dispositivos.")
    with open('dispositivos.json', 'r') as f:
        direcciones_dict = json.load(f)

    cont_gestion = 0
    cont_datos = 0
    response_gestion = []
    response_datos = []
    direcciones = 0
    print(direcciones_dict.get("gestion")[cont_gestion])
    for direcciones in direcciones_dict.get("gestion"):
        print("direcciones = " + direcciones)
        gestion = os.system("ping -n 2 " + direcciones)
        response_gestion.append(gestion)

        print("La respuesta es:")

        cont_gestion = cont_gestion + 1
        #print(direcciones.gestion)
    print(response_gestion[2])

    for direcciones in direcciones_dict.get("datos"):
        datos = os.system("ping -n 2 " + direcciones)
        response_datos.append(datos)
        cont_datos = cont_datos + 1

    print("Las direcciones de la red de gestión disponibles son: ")

    cont = 0;
    for x in response_gestion:

        if(x == 0):
            print(direcciones_dict.get("names-gestion")[cont] + " -------------> ACTIVO" )
        else:
            print(direcciones_dict.get("names-gestion")[cont] + " -------------> INACTIVO" )

        cont += 1


    print("Las direcciones de la red de datos disponibles son:")
    cont = 0
    for y in response_datos:
        if (y == 0):
            print(direcciones_dict.get("names-datos")[cont] + " -------------> ACTIVO")
        else:
            print(direcciones_dict.get("names-datos")[cont] + " -------------> INACTIVO")

        cont += 1


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
# Script para la generación de tráfico y ataques a los distintos hosts de la red CyberRange
#Author: Alberto Antonio Perales Montero

import argparse
import os

from JSONmethods import *
from GUIControllerAttack import *

from GUImethods import *

print("Por favor seleccione una opción: \n")


analizador = argparse.ArgumentParser(argument_default=argparse.SUPPRESS, description='Script para la gestión de los ataques a los hosts')
analizador.add_argument('-x', help='Sale de la aplicación', default=False, action="store_true")
#subanalizador = analizador.add_subparsers(help='comandos')
analizador.add_argument('operacion', choices=['TrafficFlow', 'Servidor', 'SSHAttack', 'Monitorizar'],  help="Permite escoger entre una de las 4 opciones descritas anteriormente")

analizador.add_argument('-o', nargs='+', type=str, dest='origen', help="Uno o más hosts origen, se requiere "
                                                                        "de indicar mediante su ip correspondiente o su nic Ejemplo: (RP_R1_1)")

group = analizador.add_mutually_exclusive_group(required=True)
group.add_argument('-a', action="store_true", dest='todos', default=False, help="Todos los dispositivos")

group1 = analizador.add_argument_group('-d')
group1.add_argument('--o', action="store", nargs='+', type=str, dest='origen', help="Uno o más hosts origen, se requiere "
                                                                        "de indicar mediante su ip correspondiente o su nic Ejemplo: (RP_R1_1)")
group1.add_argument('--h', actiohn="store", nargs='+', type=str, dest='host', help="Uno o más hosts destino, se requiere "
                                                                       "de indicar mediante su ip correspondiente o su nic Ejemplo: (RP_R1_1)")
group.add_argument(group1)
#group.add_argument('-d', nargs='+', type=str, dest='host', help="Uno o más hosts destino, se requiere "
                                                                   #     "de indicar mediante su ip correspondiente o su nic Ejemplo: (RP_R1_1)")

#group.add_argument('-d', nargs='+', choices=range(1, 6), type=int, dest='dispositivo', help="Uno o más dispositivos, se requiere "
                                                                       # "de indicar mediante su ip correspondiente o su nic(sw, wr, r1, r2, r3)")
analizador.add_argument('--version', action='version',
                    version='%(prog)s 1.0')

argumento = analizador.parse_args()
hosts = []

print(argumento)
todos = argumento.todos
if(argumento.operacion == "TrafficFlow"):
    print("Por favor introduzca la ruta correspondiente al diccionario que quiere cargar en los dispositivos origen, "
          "en caso de no dar ninguna dirección se escogerá la dirección por defecto:")
    ruta_diccionario = input()

    print("Por favor introduzca la ruta correspondiente al archivo que quiere cargar en los dispositivos origen, "
          "en caso de no dar ninguna dirección se escogerá la dirección por defecto:")
    ruta_archivo = input()

if (todos): #1er Caso si se selecciona -a significa que la acción de TrafficFlow, Servidor, SSHAttack o Monitorización
            #Corresponde a todos los hosts a los que se le puedan realizar dicha acción.
    print("He entrado en la opcion -a")
    controller(argumento.operacion, "-a")


else: #En caso contrario corresponde al número de dispositivos que escribiese el usuario por teclado
    hosts_destino = argumento.host
    hosts_origen = argumento.origen

    controller(argumento.operacion, "-h", hosts_origen, hosts_destino)

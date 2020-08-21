# Script para la generación de tráfico y ataques a los distintos hosts de la red
# CyberRange
#Author: Alberto Antonio Perales Montero

import argparse
import os

from JSONmethods import *
from GUIControllerAttack import *
from scanPorts import *

from GUImethods import *

#print("Por favor seleccione una opción: \n")


analizador = argparse.ArgumentParser(argument_default=argparse.SUPPRESS,
            description='Script para la gestión de los ataques a los hosts')

analizador.add_argument('-x', help='Sale de la aplicación',
                        default=False, action="store_true")

#subanalizador = analizador.add_subparsers(help='comandos')

analizador.add_argument('operacion', choices=['TrafficFlow', 'Scan',
                                        'Servidor', 'SSHAttack', 'Monitorizar'],
    help="Permite escoger entre una de las 4 opciones descritas anteriormente")

#analizador.add_argument('-o', nargs='+', type=str, dest='origen',
# help="Uno o más hosts origen, se requiere "
    #    "de indicar mediante su ip correspondiente o su nic Ejemplo: (RP_R1_1)")

group = analizador.add_mutually_exclusive_group(required=True)
group.add_argument('-a', action="store_true", dest='todos', default=False,
                   help="Todos los dispositivos")
group.add_argument('-d', action="store_true", dest='dispositivo',
                   help="Uno o más dispositivos, se requiere "
        "de indicar mediante su ip correspondiente o su nic(sw, wr, r1, r2, r3)")


#Opción de Scan:


group1 = analizador.add_argument_group('-d')
group1.add_argument('--o', action="store", nargs='+', type=str, dest='origen',
                    help="Uno o más hosts origen, se requiere "
        "de indicar mediante su ip correspondiente o su nic Ejemplo: (RP_R1_1)")

group1.add_argument('--h', action="store", nargs='+', type=str,
        default="0", dest='target', help="Uno o más hosts destino, se requiere "
        "de indicar mediante su ip correspondiente o su nic Ejemplo: (RP_R1_1)")

group1.add_argument('--t', action="store", nargs='+', type=str, dest='tiempo',
        default='0', help="Tiempo que durará los ataques y el tráfico (Opcional")

group1.add_argument('--s', action="store_true", default=False, dest='s',
                    help="Apagar o parar (sólo válido para Servidor y TrafficFlow")

group1.add_argument('--m', action='store', nargs='+', type=str, dest='mask',
                 help="Se debe dar el prefijo de cada una de las Ips introducidas")

#group.add_argument('-d', nargs='+', type=str, dest='host',
# help="Uno o más hosts destino, se requiere "
#     "de indicar mediante su ip correspondiente o su nic Ejemplo: (RP_R1_1)")

#group.add_argument('-d', nargs='+', choices=range(1, 6),
# type=int, dest='dispositivo', help="Uno o más dispositivos, se requiere "
        # "de indicar mediante su ip correspondiente o su nic(sw, wr, r1, r2, r3)")

analizador.add_argument('--version', action='version',
                version='%(prog)s 1.0', help="Muestra la versión de la aplicación")

argumento = analizador.parse_args()
host_destino = []
host_origen = []
mascara = []

#print(argumento)
todos = argumento.todos


if (todos): #1er Caso si se selecciona -a significa que la acción de TrafficFlow,
    # Servidor, SSHAttack o Monitorización
#Corresponde a todos los hosts a los que se le puedan realizar dicha acción.
    #print("He entrado en la opcion -a")
    controller(argumento.operacion, "-a")


else: #En caso contrario corresponde al número de
    # dispositivos que escribiese el usuario por teclado
    if(argumento.operacion == "TrafficFlow"):
        hosts_destino = argumento.target
        hosts_origen = argumento.origen
        suboperacion = ""
        #print(argumento.tiempo)
        if(argumento.tiempo == ""):
            time = 0
        else:
            time = int(argumento.tiempo)

        if(argumento.s):
            suboperacion = '--s'

        controller(argumento.operacion, "-d", hosts_origen, hosts_destino,
                   tiempo=time, suboperacion=suboperacion)

    elif(argumento.operacion == "Scan" or
         argumento.operacion == "SSHAttack"):

        host_destino = argumento.target
        host_origen = argumento.origen
        mascara = argumento.mask
        controller(argumento.operacion, "-d", host_origen,
                   host_destino, mask=mascara)
    elif(argumento.operacion == "Servidor" or
         argumento.operacion == "Monitorizar"):

        host_destino = argumento.target
        if(not argumento.s):
            suboperacion = ""
        else:
            suboperacion = "--s"
        controller(argumento.operacion, "-d", host_origen,
                   host_destino, suboperacion=suboperacion)
    elif(argumento.operacion == "Monitorizar"):
        host_destino = argumento.target
        controller(argumento.operacion, "-d", host_origen, host_destino)
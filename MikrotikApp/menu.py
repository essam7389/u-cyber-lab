# Script para recuperación de la configuración por defecto de los Routers y Switches Mikrotik
#Author: Alberto Antonio Perales Montero

import argparse
import os

from GUIController import controller
from GUImethods import *

print("Por favor seleccione una opción: \n")
print("1. Apagar Dispositivo \n"
     "2. Reiniciar Dispositivo \n"
     "3. Consultar Estado de los Dispositivos \n"
     "4. Resetear Dispositivo \n")

analizador = argparse.ArgumentParser(argument_default=argparse.SUPPRESS, description='Script para la gestión de los dispositios Mikrotik')
analizador.add_argument('-x', help='Sale de la aplicación', default=False, action="store_true")
#subanalizador = analizador.add_subparsers(help='comandos')
analizador.add_argument('operacion', choices=['Apagar', 'Reiniciar', 'Consultar', 'Resetear'],  help="Permite escoger entre una de las 4 opciones descritas anteriormente")

group = analizador.add_mutually_exclusive_group(required=True)
group.add_argument('-a', action="store_true", dest='todos', default=False, help="Todos los dispositivos")
group.add_argument('-d', nargs='+', type=str, dest='dispositivo', help="Uno o más dispositivos, se requiere "
                                                                        "de indicar mediante su ip correspondiente o su nic(sw, wr, r1, r2, r3)")

#group.add_argument('-d', nargs='+', choices=range(1, 6), type=int, dest='dispositivo', help="Uno o más dispositivos, se requiere "
                                                                       # "de indicar mediante su ip correspondiente o su nic(sw, wr, r1, r2, r3)")
analizador.add_argument('--version', action='version',
                    version='%(prog)s 1.0')


argumento = analizador.parse_args()
dispositivo = []
hosts = []

print(argumento)
todos = argumento.todos



if(argumento.x):
    print("Saliendo del programa...")
    exit()

direcciones_dict = getDevices()
#Se obtiene información referente a la autenticación de la conexión

ssh = None
keyfile_path = 'private_key_file'

##############################################################################################################

if (todos): #1er Caso si se selecciona 0 significa que la acción de Apagar, Reiniciar o Resetear corresponde a todos los dispositivos
    print("He entrado en la opcion -a")
    if(argumento.operacion != "Resetear"):
        controller(argumento.operacion, "-a")
    else:
        rutas = []

        for x in direcciones_dict.get("devices"):
            print(" Seleccione una carpeta de la lista: ")
            dir = "C:\\Users\Aru-kun\Documents\TFG\Backups";
            print(os.listdir(dir))

            print("Por favor introduzca el nombre de la carpeta a la cuál desea acceder")

            carpeta = input();
            dir = dir + carpeta;

            print(
                " Introduzca el nombre del backup que quiera cargar, tenga en cuenta que si carga un backup de manera equivocada en un dispositivo "
                "puede tener consecuencias desconocidas.: ")
            print(os.listdir(dir));

            backup = input();

            print("El backup seleccionado es= " + backup)
            print("¿Está seguro que desea cargar dicho Backup? y/n")

            confirmacion = input()

            if (confirmacion == "n"):
                print("Cancelando reseteo...")
                exit()

            ruta = dir+backup

            rutas.append(ruta)

        controller(argumento.operacion,  "-a", dispositivo, None, rutas)


else: #En caso contrario corresponde al número de dispositivos que escribiese el usuario por teclado
    dispositivo = argumento.dispositivo
    if (argumento.operacion != "Resetear"):
        print("he entrado en -d")
        #Se debe controlar que el usuario introduzca los ids, si introduce otra cosa -> Error
        controller(argumento.operacion, "-d", dispositivo, hosts)
    else:
        rutas = []
        for x in len(dispositivo):
            print(" Seleccione una carpeta de la lista: ")
            dir = "C:\\Users\Aru-kun\Documents\TFG\Backups";
            print(os.listdir(dir))

            print("Por favor introduzca el nombre de la carpeta a la cuál desea acceder")

            carpeta = input();
            dir = dir + carpeta;

            print(
                " Introduzca el nombre del backup que quiera cargar, tenga en cuenta que si carga un backup de manera equivocada en un dispositivo "
                "puede tener consecuencias desconocidas.: ")
            print(os.listdir(dir));

            backup = input();

            print("El backup seleccionado es= " + backup)
            print("¿Está seguro que desea cargar dicho Backup? y/n")

            confirmacion = input()

            if (confirmacion == "n"):
                print("Cancelando reseteo...")
                exit()

            ruta = dir + backup

            rutas.append(ruta)

        controller(argumento.operacion, "-d", dispositivo, None, rutas)

# Script para recuperación de la configuración por defecto de los Routers y Switches Mikrotik
#Author: Alberto Antonio Perales Montero
import sys

import paramiko
from paramiko import AuthenticationException, SSHException, BadHostKeyException

from tiempo import tiempo
from sshConnection import connection
from shutdown import apagar
from Reset import reset
from reboot import reboot
from estado import estado
import re
import json
import argparse

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
group.add_argument('-d', nargs='+', choices=range(1, 6), type=int, dest='dispositivo', help="Uno o más dispositivos, se requiere "
                                                                        "de indicar mediante un entero del 1 al 5 el o los dispositivos a los cuales se quiere realizar la operación")


analizador.add_argument('--version', action='version',
                    version='%(prog)s 1.0')


argumento = analizador.parse_args()
dispositivo = []

print(argumento)
todos = argumento.todos

'''if(analizador.parse_args()):
    
    print(argumento)

else:
    op = 0;
    print("Introduzca opción:")
    op = input();
    '''

#print(" argumento = " + argumento)

#argumento = analizador.parse_args()
#print("Se ha escogido:" + argumento.operacion)
if(argumento.x):
    print("Saliendo del programa...")
    exit()

#print("La opción introducida es: " + op)
if(argumento.operacion == 'Apagar'):
    print(
        "Por favor seleccione uno o varios dispositivos que desee apagar, en caso de querer varias opciones deberá introducirlas seguidamente y sin espacios. "
        "Ejemplo para el reinicio de los dispositivos 1, 2 y 3 sería = 123.")

    print("0. Todos los dispositivos \n"
          "1. Dispositivo Switch-CRS \n"
          "2. Dispositivo Router-Wifi \n"
          "3. Dispositivo Router1 \n"
          "4. Dispositivo Router2 \n"
          "5. Dispositivo Router3 \n")
elif (argumento.operacion == 'Reiniciar'):
    print(
        "Por favor seleccione uno o varios dispositivos que desee reiniciar, en caso de querer varias opciones deberá introducirlas seguidamente y sin espacios. "
        "Ejemplo para el reinicio de los dispositivos 1, 2 y 3 sería = 123.")

    print("0. Todos los dispositivos \n"
          "1. Dispositivo Switch-CRS \n"
          "2. Dispositivo Router-Wifi \n"
          "3. Dispositivo Router1 \n"
          "4. Dispositivo Router2 \n"
          "5. Dispositivo Router3 \n")


    #reboot()
elif (argumento.operacion == 'Consultar'):
    print("0. Todos los dispositivos \n"
          "1. Dispositivo Switch-CRS \n"
          "2. Dispositivo Router-Wifi \n"
          "3. Dispositivo Router1 \n"
          "4. Dispositivo Router2 \n"
          "5. Dispositivo Router3 \n")
elif (argumento.operacion == 'Resetear'):
    print(
        "Por favor seleccione uno o varios dispositivos que desee resetear, en caso de querer varias opciones deberá introducirlas seguidamente y sin espacios. "
        "Ejemplo para el reinicio de los dispositivos 1, 2 y 3 sería = 123.")

    print("0. Todos los dispositivos \n"
          "1. Dispositivo Switch-CRS \n"
          "2. Dispositivo Router-Wifi \n"
          "3. Dispositivo Router1 \n"
          "4. Dispositivo Router2 \n"
          "5. Dispositivo Router3 \n")

#analizador.add_argument("dispositivo", choices=['-a', '-s', '-w', '-r1' , '-r2', '-r3'], nargs='+', type=int, help="Elige entre la opción -a,  uno o varios dispositivos ")
#argumento = analizador.parse_args()
#print(argumento)
#patron = re.compile('[0-5]')
#dispositivo = input()




if(argumento.x):
    print("Saliendo del programa...")
    exit()

with open('dispositivos.json', 'r') as f: #Se realiza la lectura del fichero JSON
    direcciones_dict = json.load(f) #Se guardan los datos del fichero JSON en la variable direcciones_dict que nos permitirá acceder a los diversos campos del JSON

#Se obtiene información referente a la autenticación de la conexión
username = direcciones_dict.get("username")
password = direcciones_dict.get("password")
port = int(direcciones_dict.get("port"))
print(port)
print("el usuario es = " +username)
print("la pass es = "+ password)


ssh = None
keyfile_path = 'private_key_file'

'''
def connection(host, port, username, password):
    # Create the SSH client.
    try:
        ssh = paramiko.SSHClient()

        print("la dirección es = " + host)
        # Setting the missing host key policy to AutoAddPolicy will silently add any missing host keys.
        # Using WarningPolicy, a warning message will be logged if the host key is not previously known
        # but all host keys will still be accepted.
        # Finally, RejectPolicy will reject all hosts which key is not previously known.
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        # Connect to the host.

        ssh.connect(host, port, username, password, timeout=4)


        print("Conexión realizada")

        #tm = tiempo.tiempo()  # Calculamos el tiempo pasado en segundos desde el año 1970
    except AuthenticationException:
        print("Authentication failed, please verify your credentials: %s")
        sys.exit(1)
    except SSHException as sshException:
        print("Unable to establish SSH connection: %s" % sshException)
        sys.exit(1)
    except BadHostKeyException as badHostKeyException:
        print("Unable to verify server's host key: %s" % badHostKeyException)
        sys.exit(1)
    except Exception:
        print("Ha ocurrido un error al intentar conectar con el dispositivo")
        exit()

    return (ssh)

'''
#print("El patron del dispositivo es = ")
#print(patron.search(dispositivo))

#if (patron.findall(dispositivo, 0,4)): #Se comprueba que lo que el usuario ha enviado por teclado corresponde con la expresión regular

    # argumento = analizador.parse_args()
print(todos)
#numero = int(dispositivo) #Se pasa el string a entero

if (todos): #1er Caso si se selecciona 0 significa que la acción de Apagar, Reiniciar o Resetear corresponde a todos los dispositivos
    print("He entrado en la opcion -a")
    if(argumento.operacion == "Apagar"):

        for direccion in direcciones_dict.get("devices"):
            ip = direccion.get("nics")['management']['IP']
            ssh = connection(ip, port, username, password)
            apagar(ssh)

    elif(argumento.operacion=="Reiniciar"):
        for direccion in direcciones_dict.get("devices"):
            ip = direccion.get("nics")['management']['IP']
            ssh = connection(ip, port, username, password)
            reboot(ssh)
    elif(argumento.operacion=="Resetear"):
        for direccion in direcciones_dict.get("devices"):
            ip = direccion.get("nics")['management']['IP']
            ssh = connection(ip, port, username, password)
            reset(ssh, ip, port, username, password)

    elif(argumento.operacion == "Consultar"):
        estado((dispositivo))



else: #En caso contrario corresponde al número de dispositivos que escribiese el usuario por teclado
    dispositivo = argumento.dispositivo
    cont = 0
    if (argumento.operacion == "Apagar"):

        while (cont < len(dispositivo)): #Mientras el contador (que comienza en 0) sea < el nº de direcciones que hay en el JSON itera.
            numero = dispositivo[cont]
            ip = direcciones_dict.get("devices")[numero-1].get("nics")['management']['IP']#Se le resta 1 porque al acceder al JSON la primera posición es la 0
            ssh = connection(ip, port, username, password) #Se llama a connection y se obtiene la conexión ssh para una dirección de dispositivo dada.
            apagar(ssh) #Se llama a la función apagar que apagará el dispositivo enviándo el comando mediante dicha conexión ssh
            cont += 1

    elif (argumento.operacion == "Reiniciar"):
        while (cont < len(dispositivo)):
            numero = dispositivo[cont]
            print("El numero es = ")
            print(numero)
            ip = direcciones_dict.get("devices")[numero-1].get("nics")['management']['IP'] #Se le resta 1 porque al acceder al JSON la primera posición es la 0
            print("La dirección del dispositivo a reiniciar es = " + ip)
            ssh = connection(ip, port, username, password)
            reboot(ssh)
            cont += 1
    elif (argumento.operacion == "Resetear"):
        while (cont < len(dispositivo)):
            numero = dispositivo[cont]
            ip = direcciones_dict.get("devices")[numero - 1].get("nics")['management']['IP']#Se le resta 1 porque al acceder al JSON la primera posición es la 0
            ssh = connection(ip, port, username, password)
            reset(ssh, ip, port, username, password)
            cont += 1

    elif (argumento.operacion == "Consultar"):
        estado(dispositivo)

'''
else: #En caso contrario imprime error
    print("Error, vuelva al menú y seleccione de nuevo la opción que quiere.")

'''


   # print("Restaurando...")





'''
Cuestiones:

    1. Mejora de código: Se puede establecer la definición de la función "Connection" en un archivo aparte de tal forma que
        se pueda llamar a dicha función sin perder la conexión (variable ssh en memoria). Esto posibilitaría la mejora del código y
        su legibilidad ya qué nos permitiría eliminar los bucles y quedarnos con solo dos posibles casos de instrucciones condicionales.
        Una de ellas se encargaría de comprobar la operación (todos o un dispositivo concreto) y la otra de seleccionar la acción concreta
        (Apagar, Reiniciar...), de tal forma que enviaríamos la operación como un argumento de dicha llamada a función realizando así los bucles
        y la instrucción condicional dentro de la acción concreta.
        
    2.  Mejora de Menú: Se puede establecer como segunda opción un menú mediante terminal de comandos, más interactivo y obviando argparse como se
        realizó en versiones anteriores con la salvedad de que el usuario podrá elegir entre un modo u otro (argparse o normal)
        
    3. Pregunta de tribunal: ¿Por qué has usado Python? ¿Por qué has realizado el código de estructurada (paradigma estructurado) en vez de con un paradigma 
        orientado a objetos?



'''
# Script para recuperación de la configuración por defecto de los Routers y Switches Mikrotik
#Author: Alberto Antonio Perales Montero
import paramiko
from tiempo import tiempo
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

analizador = argparse.ArgumentParser(description='Script para la gestión de los dispositios Mikrotik')
analizador.parse_args()

    #analizador.add_argument('-x', help='Sale de la aplicación', action= exit())
op = 0;
print("Introduzca opción:")
op = input();

print("La opción introducida es: " + op)
if(op == '1'):
    print(
        "Por favor seleccione uno o varios dispositivos que desee apagar, en caso de querer varias opciones deberá introducirlas seguidamente y sin espacios. "
        "Ejemplo para el reinicio de los dispositivos 1, 2 y 3 sería = 123.")

    print("0. Todos los dispositivos \n"
          "1. Dispositivo Switch-CRS \n"
          "2. Dispositivo Router-Wifi \n"
          "3. Dispositivo Router1 \n"
          "4. Dispositivo Router2 \n"
          "5. Dispositivo Router3 \n")
elif (op == '2'):
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
elif (op == '3'):
    estado()
elif (op == '4'):
    print(
        "Por favor seleccione uno o varios dispositivos que desee resetear, en caso de querer varias opciones deberá introducirlas seguidamente y sin espacios. "
        "Ejemplo para el reinicio de los dispositivos 1, 2 y 3 sería = 123.")

    print("0. Todos los dispositivos \n"
          "1. Dispositivo Switch-CRS \n"
          "2. Dispositivo Router-Wifi \n"
          "3. Dispositivo Router1 \n"
          "4. Dispositivo Router2 \n"
          "5. Dispositivo Router3 \n")


patron = re.compile('[0-5]')
dispositivo = input()

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


def connection(host, port, username, password):
    # Create the SSH client.
    ssh = paramiko.SSHClient()

    print("la dirección es = " + host)
    # Setting the missing host key policy to AutoAddPolicy will silently add any missing host keys.
    # Using WarningPolicy, a warning message will be logged if the host key is not previously known
    # but all host keys will still be accepted.
    # Finally, RejectPolicy will reject all hosts which key is not previously known.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    # Connect to the host.
    ssh.connect(host, port, username, password)

    print("Conexión realizada")
    #tm = tiempo.tiempo()  # Calculamos el tiempo pasado en segundos desde el año 1970

    return(ssh)
print("El patron del dispositivo es = ")
print(patron.search(dispositivo))

if (patron.findall(dispositivo, 0,4)): #Se comprueba que lo que el usuario ha enviado por teclado corresponde con la expresión regular
    numero = int(dispositivo) #Se pasa el string a entero
    if (dispositivo == "0"): #1er Caso si se selecciona 0 significa que la acción de Apagar, Reiniciar o Resetear corresponde a todos los dispositivos
        if(op == "1"):

            for direccion in direcciones_dict.get("gestion"):
                ssh = connection(direccion, port, username, password)
                apagar(ssh)

        elif(op=="2"):
            for direccion in direcciones_dict.get("gestion"):
                ssh = connection(direccion, port, username, password)
                reboot(ssh)
        elif(op=="3"):
            for direccion in direcciones_dict.get("gestion"):
                ssh = connection(direccion, port, username, password)
                reset(ssh, direccion, port, username, password)


    else: #En caso contrario corresponde al número de dispositivos que escribiese el usuario por teclado
        cont = 0
        if (op == "1"):

            while (cont < len(dispositivo)): #Mientras el contador (que comienza en 0) sea < el nº de direcciones que hay en el JSON itera.
                numero = int(dispositivo[cont])
                direccion = direcciones_dict.get("gestion")[numero-1]#Se le resta 1 porque al acceder al JSON la primera posición es la 0
                ssh = connection(direccion, port, username, password) #Se llama a connection y se obtiene la conexión ssh para una dirección de dispositivo dada.
                apagar(ssh) #Se llama a la función apagar que apagará el dispositivo enviándo el comando mediante dicha conexión ssh
                cont += 1

        elif (op == "2"):
            while (cont < len(dispositivo)):
                numero = int(dispositivo[cont])
                print("El numero es = ")
                print(numero)
                direccion = direcciones_dict.get("gestion")[numero-1] #Se le resta 1 porque al acceder al JSON la primera posición es la 0
                print("La dirección del dispositivo a reiniciar es = " + direccion)
                ssh = connection(direccion, port, username, password)
                reboot(ssh)
                cont += 1
        elif (op == "3"):
            while (cont < len(dispositivo)):
                numero = int(dispositivo[cont])
                direccion = direcciones_dict.get("gestion")[numero-1]#Se le resta 1 porque al acceder al JSON la primera posición es la 0
                ssh = connection(direccion, port, username, password)
                reset(ssh,direccion, port, username, password)
                cont += 1


else: #En caso contrario imprime error
    print("Error, vuelva al menú y seleccione de nuevo la opción que quiere.")


   # print("Restaurando...")

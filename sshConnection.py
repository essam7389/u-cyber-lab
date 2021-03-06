# Script para recuperación de la configuración por defecto de los Routers y Switches Mikrotik
#Author: Alberto Antonio Perales Montero
import sys

from tiempo import tiempo
import os
import paramiko
from paramiko import SSHClient, AuthenticationException, SSHException, BadHostKeyException

ssh = None
keyfile_path = 'private_key_file'



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
def connection(host, port, username, password):

    print("Se va a realizar la conexión con el Switch CSR de Mikrotik.");
    print("¿Está seguro? S/N");


    #while(respuesta != "N" or respuesta != "S"):
    respuesta = input();

    if (respuesta == "N" or respuesta != "S"):
        print("Se ha cancelado la conexión");
        exit();

    elif (respuesta == "S"):
       # print("Restaurando...")

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

        stdin, stdout1, stderr = ssh.exec_command('/system clock set time=' + tiempo())
        stdin, stdout2, stderr = ssh.exec_command('/system clock set print')


    return(ssh)

'''


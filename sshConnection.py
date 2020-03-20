# Script para recuperación de la configuración por defecto de los Routers y Switches Mikrotik
#Author: Alberto Antonio Perales Montero

from tiempo import tiempo
import os
import paramiko
from paramiko import SSHClient
from scp import SCPClient
from shutdown import apagar
from Reset import reset
from reboot import reboot
from estado import estado


ssh = None

host = '192.168.2.1'
port = 22
username = 'admin'
password = ''
keyfile_path = 'private_key_file'

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

    print("Por favor seleccione una opción: \n")
    print("1. Apagar Dispositivo \n"
         "2. Reiniciar Dispositivo \n"
         "3. Consultar Estado de los Dispositivos \n"
         "4. Resetear Dispositivo \n")

    op = 0;
    print("Introduzca opción:")
    op = input();
    print("La opción introducida es: " + op)
    if(op == '1'):
      apagar(ssh)
    elif (op == '2'):
        reboot(ssh)
    elif (op == '3'):
        estado(ssh)
    elif (op == '4'):
        reset(ssh, host, port, username, password)

ssh.close()
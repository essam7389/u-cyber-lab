import scp as scp
from scp import SCPClient
from sshConnection import *

def updateFile(ssh, ruta_archivo, sistema, nombre):
    '''

    :param ssh: Recibe una conexión SSH
    :param ruta_archivo: Recibe la ruta absoluta donde se encuentra el archivo que se quiere cargar
    :param sistema: Recibe el sistema operativo al cuál se va a cargar dicho archivo, que puede ser Kali Linux o Ubuntu Mate
    :param nombre: Recibe el nombre que se le dará al archivo que se quiere cargar.
    :return: No devuelve nada
    '''
    scp = SCPClient(ssh.get_transport())

    if(sistema == "kali"):
        #Para Kali Linux
        scp.put(ruta_archivo,  remote_path='/root/Documents/script/' + nombre);
    elif(sistema == "mate"):
        #Para ubuntu mate
        scp.put(ruta_archivo,  remote_path='/home/ucase/Documentos/'+nombre);

    ssh.close()


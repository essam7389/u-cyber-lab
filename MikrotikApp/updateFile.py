import scp as scp
from scp import SCPClient
from sshConnection import *

def updateFile(ssh, ruta_archivo, sistema, nombre):

    scp = SCPClient(ssh.get_transport())

    if(sistema == "kali"):
        #Para Kali Linux
        scp.put(ruta_archivo,  remote_path='/root/Documents/script/' + nombre);
    elif(sistema == "mate"):
        #Para ubuntu mate
        scp.put(ruta_archivo,  remote_path='/home/ucase/Documentos/'+nombre);

    ssh.close()


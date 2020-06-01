from tkinter import messagebox

from scp import SCPClient
from GUImethods import mensajeError

def updateFile(ssh, ruta_origen, sistema = "", ruta_destino = ""):
    '''
    :param ssh: Recibe una conexión ssh activa
    :param ruta_origen: Se recibe la ruta de origen del archivo a subir
    :param sistema: Se recibe el sistema operativo al cuál se va a subir el archivo
    :param ruta_destino: Se recibe la ruta de destino del archivo a subir
    :return: No devuelve nada
    '''

    try:

        scp = SCPClient(ssh.get_transport())
        ruta_defecto_kali = "/root/Documents/scripts/"
        ruta_defecto_ubuntu = "/home/ucase/Documentos/scripts/"
        print("sistema = " + sistema)
        print("ruta_destino = " + ruta_destino)
        if(sistema == "Kali Linux" and ruta_destino == ""): #Para Kali Linux
            print("He entrado en ruta_destino == """)
            ruta_destino = ruta_defecto_kali;
        elif(sistema == "Ubuntu Mate" and ruta_destino == ""): #Para ubuntu mate
            ruta_destino = ruta_defecto_ubuntu;

        #ruta_destino += nombre
        print("ruta origen = " + ruta_origen)
        print("ruta destino = " + ruta_destino)
        scp.put(ruta_origen, remote_path=ruta_destino);
        scp.close()
    except Exception:
        msgerror = "Ha ocurrido un error al intentar cargar el archivo en el dispositivo"
        titulo = "Error al conectar"
        print(msgerror)
        mensajeError(msgerror, titulo)
        exit()



'''
if(accion == "TrafficFlow"):
    scp.put(ruta_origen,  remote_path=ruta_destino);

elif(accion == "SSHAttack"):
    if (sistema == "Kali Linux"):
        print("He entrado en SCP opcion SSHAttack")
        # Para Kali Linux
        scp.put(ruta_origen, remote_path='/root/Documents/Diccionarios/' + nombre);

    elif (sistema == "Ubuntu Mate"):
        # Para ubuntu mate
        scp.put(ruta_origen, remote_path='/home/ucase/Documentos/Diccionarios' + nombre);


'''

'''
port = 22
print("Indique el tipo de sistema:")
print("kali o mate")

sistema = input()

print("Introduzca la ip del dispositivo ")

host = input()

print("Introduzca el usuario: ")

username = input()

print("Introduce la contraseña: ")

password = input()

ssh = connection(host, port, username, password)
print("Introduzca la ruta donde se encuentra el backup que desea subir")
ruta = input()

print("Seleccione un nombre alternativo para el fichero: ")
nombre = ""
while(nombre == ""):
    nombre = input()


scp = SCPClient(ssh.get_transport())

if(sistema == "kali"):
    #Para Kali Linux
    scp.put(ruta,  remote_path='/root/Documents/script/' + nombre);
elif(sistema == "mate"):
    #Para ubuntu mate
    scp.put(ruta,  remote_path='/home/ucase/Documentos/'+nombre);

ssh.close()


'''
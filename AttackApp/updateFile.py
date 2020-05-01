from scp import SCPClient

def updateFile(ssh, accion, ruta_archivo, sistema, nombre):

    scp = SCPClient(ssh.get_transport())

    if(accion == "TrafficFlow"):
        if(sistema == "Kali Linux"):
            #Para Kali Linux
            scp.put(ruta_archivo,  remote_path='/root/Documents/script/' + nombre);
        elif(sistema == "Ubuntu Mate"):
            #Para ubuntu mate
            scp.put(ruta_archivo,  remote_path='/home/ucase/Documentos/'+nombre);
    elif(accion == "SSHAttack"):
        if (sistema == "Kali Linux"):
            print("He entrado en SCP opcion SSHAttack")
            # Para Kali Linux
            scp.put(ruta_archivo, remote_path='/root/Documents/Diccionarios/' + nombre);

        elif (sistema == "Ubuntu Mate"):
            # Para ubuntu mate
            scp.put(ruta_archivo, remote_path='/home/ucase/Documentos/Diccionarios' + nombre);



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
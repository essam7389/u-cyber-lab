from scp import SCPClient

from sshConnection import connection

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
    scp.put(ruta,  remote_path='/root/Documents/' + nombre);
elif(sistema == "mate"):
    #Para ubuntu mate
    scp.put(ruta,  remote_path='/home/ucase/Documentos/'+nombre);

ssh.close()

from tkinter import *
import importlib

import paramiko
from tiempo import tiempo
from shutdown import apagar
from Reset import reset
from reboot import reboot
from sshConnection import connection
from estado import estado

host = '172.16.1.1'
port = 22
username = 'admin'
password = ''
'''
def connection():
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
    # tm = tiempo.tiempo()  # Calculamos el tiempo pasado en segundos desde el año 1970

    stdin, stdout1, stderr = ssh.exec_command('/system clock set time=' + tiempo(ssh))
    stdin, stdout2, stderr = ssh.exec_command('/system clock set print')

    return (ssh)
'''
ssh = None


def reinicio():
    rebootWindow = Toplevel(raiz)
    rebootWindow.title("Consultar Dispositivos")
    rebootWindow.wm_resizable(0, 0)
    rebootWindow.geometry("400x150")

    return "hola"

#ssh = connection() #LLamamos a la función connection que nos devolverá una conexión ssh realizada al dispositivo
raiz = Tk() #Llamamos al constructor de tkinter que nos devolverá un objeto de tipo tkinter al que llamaremos raiz(esta será nuestra ventana/GUI en sí)
#Título de la interfáz gráfica
raiz.title("GUI-Mikrotik")
#Función para el tamaño de la ventana
raiz.resizable(0,0)
#Cambio del icono predeterminado
icono = PhotoImage(file='gui-icon.png')
raiz.iconphoto(False, icono)
#raiz.wm_iconbitmap("gui-icon.ico"); #/GUI-Mikrotik/Iconos/gui-icon.icon


raiz.geometry("500x400")#Le damos a la ventana un tamaño en ancho y alto
foto = PhotoImage(file="gui-icon.png")
Label(raiz, image=foto).pack()

frame = Frame(raiz) #Creamos un frame
frame.pack(fill="both" ,expand="true", pady=15)    #Empaquetamos el frame dentro de la ventana
frame.config(width="600", height="300", cursor="pirate")
#A partir de aquí vamos creando los botones correspondientes a las diferentes opciones:

btnShutdown = Button(frame, text="Apagar Dispositivos", justify= CENTER, command=lambda: apagar(ssh))
btnReboot = Button(frame, text="Reiniciar Dispositivos", justify= CENTER, command=lambda: reinicio())
btnReset = Button(frame, text="Resetear Dispositivos", justify= CENTER, command=lambda: reset(ssh, host, port, username, password))
btnEstado = Button(frame, text="Consultar Estado de los Dispositivos", justify= CENTER, command=lambda: estado(ssh))

btnShutdown.pack(fill="x", padx=10, pady=10)
btnReboot.pack(fill="x", padx=10, pady=10)
btnReset.pack(fill="x",  padx=10, pady=10)
btnEstado.pack(fill="x",  padx=10, pady=10)

raiz.mainloop()



    
from tkinter import *
from GUIScan import *
from GUISSHAttack import *
from GUITraffic import *
from GUIServidor import *
from GUIMonitorizar import *

ssh = None

#ssh = connection() #LLamamos a la función connection que nos devolverá una conexión ssh realizada al dispositivo
raiz = Tk() #Llamamos al constructor de tkinter que nos devolverá un objeto de tipo tkinter al que llamaremos raiz(esta será nuestra ventana/GUI en sí)
#Título de la interfáz gráfica
raiz.title("GUI-Attack")
#Función para el tamaño de la ventana
raiz.resizable(0,0)
#Cambio del icono predeterminado
icono = PhotoImage(file='gui-icon-attack2.png')
raiz.iconphoto(False, icono)

raiz.geometry("500x500")#Le damos a la ventana un tamaño en ancho y alto
foto = PhotoImage(file="gui-icon-attack2.png")
Label(raiz, image=foto).pack()

frame = Frame(raiz) #Creamos un frame
frame.pack(fill="both" ,expand="true", pady=15)    #Empaquetamos el frame dentro de la ventana
frame.config(width="600", height="300", cursor="pirate")
#A partir de aquí vamos creando los botones correspondientes a las diferentes opciones:

btnScan = Button(frame, text="Escanear Red", justify=CENTER, command=lambda: scan(raiz))
btnTraffic = Button(frame, text="Generar Tráfico", justify=CENTER, command=lambda: generateTraffic(raiz))
btnSshAttack = Button(frame, text="SSH Attack", justify=CENTER, command=lambda: sshAttack(raiz))


btnServer = Button(frame, text="Activar Servidores", justify=CENTER, command=lambda: servers(raiz))
btnMonitorizar = Button(frame, text="Monitorizar", justify=CENTER, command=lambda: monitorizar(raiz))

btnScan.pack(fill="x", padx=10, pady=10)
btnTraffic.pack(fill="x", padx=10, pady=10)
btnSshAttack.pack(fill="x",  padx=10, pady=10)
btnServer.pack(fill="x",  padx=10, pady=10)
btnMonitorizar.pack(fill="x",  padx=10, pady=10)

raiz.mainloop()
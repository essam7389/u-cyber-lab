from tkinter import *
import GUIScan as escanear
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
icono = PhotoImage(file='attackIcon.png')
raiz.iconphoto(False, icono)

raiz.geometry("500x500")#Le damos a la ventana un tamaño en ancho y alto
foto = PhotoImage(file="attackIcon.png")
Label(raiz, image=foto).pack()

frame = Frame(raiz) #Creamos un frame
frame.pack(fill="both", expand="true", pady=15)    #Empaquetamos el frame dentro de la ventana
frame.config(width="600", height="300", cursor="pirate")
#A partir de aquí vamos creando los botones correspondientes a las diferentes opciones:

btnScan = Button(frame, text="Escanear Red", justify=CENTER, command=lambda: escanear.scan(raiz))
btnTraffic = Button(frame, text="Activar/Desactivar Tráfico", justify=CENTER, command=lambda: generateTraffic(raiz))
btnSshAttack = Button(frame, text="Ataque SSH", justify=CENTER, command=lambda: sshAttack(raiz))
btnServer = Button(frame, text="Activar/Desactivar Servidores", justify=CENTER, command=lambda: servers(raiz))
btnMonitorizar = Button(frame, text="Monitorizar", justify=CENTER, command=lambda: monitorizar(raiz))

#Se generan los botones en la interfáz de manera gráfica
btnScan.pack(fill="x", padx=10, pady=10)
btnTraffic.pack(fill="x", padx=10, pady=10)
btnSshAttack.pack(fill="x",  padx=10, pady=10)
btnServer.pack(fill="x",  padx=10, pady=10)
btnMonitorizar.pack(fill="x",  padx=10, pady=10)

raiz.mainloop()



#1. Para solucionar el problema de la barra de carga tenemos que crear una función intermedia entre la función controller
#y la interfáz gráfica, esto es debido a qué así terminamos la ejecución de dicha ventana hija de la aplicación y podemos
#abrir otras ventanas y envíar los datos a la función controller

# 2. Para el caso de la scrollbar en la ventana para añadir datos a los diccionarios debemos fijarnos en la lista de checksButtons
#que tenemos en cualquiera de las ventanas de la GUI y cambiar los checksButtons por Entrys y Labels, además ampliando la superficie.
# Una vez hecho esto, tanto en la opción de editar como de eliminar podemos pedir al usuario el nic del dispositivo de tal forma
#que una vez el usuario pulse fuera del Entry se evalue dicho nic con los que hay en los diccionarios, si lo encuentra devuelve
#True habilitando cada uno de los campos a rellenar del dispositivo o en caso contrario devolviendo false y no habilitándolos.
#Para eliminar un dispositivo simplemente se comprobaría si el nic es true y se eliminaría.
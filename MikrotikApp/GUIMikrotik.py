from tkinter import *
from GUIreinicio import reinicio
from GUIapagado import apagado
from GUIreseteo import reseteo
from GUIconsulta import estado
from GUICreate import *
from GUIEditar import *
ssh = None

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


raiz.geometry("500x450")#Le damos a la ventana un tamaño en ancho y alto
foto = PhotoImage(file="gui-icon.png")
Label(raiz, image=foto).pack()

menu = Menu(raiz)

new_item = Menu(menu)

menu.add_cascade(label='Diccionarios', menu=new_item)
new_item.add_command(label='Añadir', command=lambda: addDiccionario(raiz), accelerator="Ctrl+a")
new_item.add_separator()
new_item.add_command(label='Editar', command=lambda: editDiccionario(raiz), accelerator="Ctrl+e")
new_item.add_separator()
new_item.add_command(label='Eliminar')


raiz.config(menu=menu)

frame = Frame(raiz) #Creamos un frame
frame.pack(fill="both" ,expand="true", pady=15)    #Empaquetamos el frame dentro de la ventana
frame.config(width="600", height="300", cursor="pirate")
#A partir de aquí vamos creando los botones correspondientes a las diferentes opciones:

btnShutdown = Button(frame, text="Apagar Dispositivos", justify= CENTER, command=lambda: apagado(raiz))
btnReboot = Button(frame, text="Reiniciar Dispositivos", justify= CENTER, command=lambda: reinicio(raiz))
btnReset = Button(frame, text="Resetear Dispositivos", justify= CENTER, command=lambda: reseteo(raiz))
btnEstado = Button(frame, text="Consultar Estado de los Dispositivos", justify= CENTER, command=lambda: estado(raiz))

btnShutdown.pack(fill="x", padx=10, pady=10)
btnReboot.pack(fill="x", padx=10, pady=10)
btnReset.pack(fill="x",  padx=10, pady=10)
btnEstado.pack(fill="x",  padx=10, pady=10)

raiz.mainloop()



    
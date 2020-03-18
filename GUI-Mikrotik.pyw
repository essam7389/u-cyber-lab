from tkinter import *
import importlib

from shutdown import apagar


raiz = Tk()
#Título de la interfáz gráfica
raiz.title("GUI-Mikrotik")
#Función para el tamaño de la ventana
raiz.resizable(0,0)
#Cambio del icono predeterminado
icono = PhotoImage(file='gui-icon.png')
raiz.iconphoto(False, icono)
#raiz.wm_iconbitmap("gui-icon.ico"); #/GUI-Mikrotik/Iconos/gui-icon.icon

raiz.geometry("800x450")

btnShutdown = Button(raiz, text="Apagar Dispositivos", command=apagar)

btnShutdown.grid(column=1, row = 0);


raiz.mainloop()


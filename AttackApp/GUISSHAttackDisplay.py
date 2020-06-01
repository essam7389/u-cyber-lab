from tkinter import *


def imprimirSSHAttackGUI(raiz, stdout):
    '''
    :param raiz: Recibe una dirección a la interfáz gráfica principal de la aplicación
    :param stdout: Se recibe la salida del ataque SSH
    :return:
    '''

    #Se crea la ventana donde se imprimirá la información de salida del ataque ssh
    displayWindow = Toplevel(raiz)
    displayWindow.title("Display SSHAttack hosts")
    displayWindow.wm_resizable(0, 0)
    displayWindow.geometry("400x320")

    scrollbar = Scrollbar(displayWindow)
    text = Text(displayWindow, yscrollcommand=scrollbar.set)

    scrollbar.pack(side=RIGHT, fill=Y)
    text.pack(side=LEFT, fill=Y)

    #Se recorre la salida estandar imprimiendo todo lo que contiene
    for line in stdout:
        salida = line.strip('\n')
        print(salida)
        text.insert(INSERT, salida + "\n")


    text.config(background= "black", foreground="green")
    scrollbar.config(command=text.yview)
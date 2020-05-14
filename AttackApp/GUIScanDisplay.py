from tkinter import *


def imprimirScanGUI(raiz, names, response_gestion, response_datos, ips_gestion, ips_datos):
    displayWindow = Toplevel(raiz)
    displayWindow.title("Consultar Dispositivos")
    displayWindow.wm_resizable(0, 0)
    displayWindow.geometry("400x320")

    scrollbar = Scrollbar(displayWindow)
    text = Text(displayWindow, yscrollcommand=scrollbar.set)
    text.pack(side=LEFT, fill=Y)
    scrollbar.pack(side=RIGHT, fill=Y)
    text.insert(INSERT, " Nombre      |        IP        |       Estado      \n")
    text.insert(INSERT, " ----------------------------------------------------\n")
    text.insert(INSERT, " \n")

    cont = 0;
    i = 0
    y = response_gestion

    print("names = " + names[cont])

    for x in ips_gestion:
        if (x != "0.0.0.0" and y[i] == 0):
            ip = x
            text.insert(INSERT, "" + names[cont] + "         " + ip + "        ACTIVO\n")

        elif (x != "0.0.0.0"):
            ip = x
            text.insert(INSERT, "" + names[cont] + "         " + ip + "        INACTIVO\n")
        i += 1
        cont += 1

    cont = 0
    i = 0
    y = response_datos
    for x in ips_datos:
        if (x != "0.0.0.0" and y[i] == 0):
            ip = x
            text.insert(INSERT, "" + names[cont] + "         " + ip + "        ACTIVO\n")
        elif (x != "0.0.0.0"):
            ip = x
            text.insert(INSERT, "" + names[cont] + "         " + ip + "        INACTIVO\n")

        i += 1
        cont += 1


    text.config(background= "black", foreground="green")
    scrollbar.config(command=text.yview)

    text.insert(END, "#####################################################################")

from GUIController import controller
from GUImethods import *


def addDiccionario(raiz):
    createWindow = Toplevel(raiz)
    createWindow.title("Apagar Dispositivos")
    createWindow.wm_resizable(0, 0)
    createWindow.geometry("400x250")

    # Se crea una lista compuesta de texto y una scrollbar(barra) vertical
    formulario = Frame(createWindow)
    scrollbar = Scrollbar(formulario)
    scrollbar.pack(side=RIGHT, fill=Y, pady=20)

    list = Text(formulario, height=20, width=15)

    # Se generan los botones Check en base a la cantidad de dispositivos que haya en nuestro diccionario.
    variables_entry = []
    # variables_hosts = []
    v = 0
    i = 1
    c = 0
    entryText = []
    ids_devices = []
    labels = ["Introduzca el nombre de usuario para acceder al dispositivo o host", "Introduzca la contraseña para acceder al dispositivo o host"]

    Label(list, text=labels[0]).pack()
    Entry(list)
    list.window_create("end", window=entryText[c])
    list.insert("end", "\n")

    list.pack(pady=20)
    list.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=list.yview)

    # disable the widget so users can't insert text into it
    list.configure(state="disabled")

    # Botón de confirmación que pasa a la función controller 3 argumentos (la acción (Apagar), la operación deseada y los valores de los checks en ID
    list.pack()
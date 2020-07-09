from GUIController import controller
from GUIControllerDiccionario import controllerDiccionario
from GUImethods import *


def editDiccionario(raiz):
    editWindow = Toplevel(raiz)
    editWindow.title("Editar el Diccionario")
    editWindow.wm_resizable(0, 0)
    editWindow.geometry("800x400")

    op = IntVar()
    # Texto previo a las opciones básicas
    Label(editWindow, text="Por favor seleccione una opción: ").pack()
    # Opciones básicas, se debe elegir una u otra pero no ambas

    scan_all = Radiobutton(editWindow, text="Editar dispositivo",
                           variable=op, value=1,
                           command=lambda: disabled(entryHosts))
    scan_single = Radiobutton(editWindow, text="Editar host",
                              variable=op, value=2,
                              command=lambda: enabled(entryHosts))

    scan_all.pack()
    scan_single.pack()

    # Acción correspondiente a la opción escogida en el menú principal que se le pasará al controlador
    accion = "Editar"

    Label(editWindow, text="Por favor introduzca el identificador del dispositivo o host que desea editar \n").pack()
    id_edit = StringVar()

    Entry(editWindow, textvariable=id_edit).pack()

    # Se crea una lista compuesta de texto y una scrollbar(barra) vertical
    lista = Frame(editWindow)
    scrollbar = Scrollbar(lista)
    scrollbar.pack(side=RIGHT, fill=Y, pady=20)

    entrylist = Text(lista, height=20, width=150)

    # Variables para cada uno de los Entrys
    usuario = StringVar()
    password = StringVar()
    puerto = IntVar()
    descripcion = StringVar()
    id = StringVar()
    ip_management = StringVar()
    type_management = StringVar()
    nicname_management = StringVar()
    id_management = StringVar()
    ip_data = StringVar()
    type_data = StringVar()
    nicname_data = StringVar()
    id_data = StringVar()
    team = StringVar()
    tipo = StringVar()
    so = StringVar()


    variables = [usuario, password, puerto, descripcion, id, ip_management, type_management, nicname_management, id_management,
                 ip_data, type_data, nicname_data, id_data, team, tipo, so]
    # variables_hosts = []

    v = 0
    i = 0
    c = 0
    entrys = []
    entryHosts = []
    labels_hosts = ["Introduzca el team correspondiente al host: \n \n",
              "Introduzca el tipo de host: \n \n", "Introduzca el sistema operativo que tiene el host: \n \n"]

    labels = ["Introduzca el nombre de usuario para acceder al dispositivo o host: \n \n", "Introduzca la contraseña para acceder al dispositivo o host: \n \n",
              "Introduzca el puerto para acceder al dispositivo o host: \n \n", "Introduzca la descripción del dispositivo o host \n \n",
              "Introduzca el ID del dispositivo o host: \n \n", "Introduzca la ip correspondiente a la red de gestión: \n \n",
              "Introduzca el tipo correspondiente a la red de gestión: \n \n", "Introduzca el nic correspondiente a la red de gestión: \n \n",
              "Introduzca el id correspondiente a la red de gestión: \n \n", "Introduzca la ip correspondiente a la red de datos: \n \n",
              "Introduzca el tipo correspondiente a la red de datos: \n \n", "Introduzca el nic correspondiente a la red de datos: \n \n",
              "Introduzca el id correspondiente a la red de datos \n \n"]

    #Bucle que recorre las etiquetas correspondientes a los dispositivos, añadiendo un label y un entry por cada campo del formulario
    for label in labels:
        entrys.append(
            Entry(entrylist, text=label, textvariable=variables[c]))
        entrylist.insert("end", label)
        entrylist.window_create("end", window=entrys[c])
        entrylist.insert("end", "\n \n")
        c += 1

    # Bucle que recorre las etiquetas correspondientes a los hosts, añadiendo un label y un entry por cada campo del formulario
    for label in labels_hosts:
        entryHosts.append(
            Entry(entrylist, text=label, textvariable=variables[c], state=DISABLED))
        entrylist.insert("end", label)
        entrylist.window_create("end", window=entryHosts[i])
        entrylist.insert("end", "\n \n")
        i += 1
        c += 1

    entrylist.pack(pady=20)
    entrylist.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=entrylist.yview)

    # disable the widget so users can't insert text into it
    entrylist.configure(state="disabled")

    # Botón de confirmación que pasa a la función controller 3 argumentos (la acción (Scan), la operación deseada y los valores de los checks en ID
    btnConfirmation = Button(editWindow, text="Confirmar acción",
                             command=lambda: [controllerDiccionario(accion, id_edit, variables)])

    btnConfirmation.pack()
    btnConfirmation.pack(pady=20)

    lista.pack()
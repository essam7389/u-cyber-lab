from GUIController import controller
from GUImethods import *


def apagado(raiz):
    '''
    :param raiz: Recibe la dirección de memoria de la ventana principal
    :return: No devuelve nada
    '''
    shutdownWindow = Toplevel(raiz)
    shutdownWindow.title("Apagar Dispositivos/Hosts")
    shutdownWindow.wm_resizable(0, 0)
    shutdownWindow.geometry("400x250")
    icono = PhotoImage(file='gui-icon.png')
    shutdownWindow.iconphoto(False, icono)

    frame_reinicio = Frame(shutdownWindow)
    # frame.pack(fill="both", expand="true", pady=15)  # Empaquetamos el frame dentro de la ventana
    # frame.config(width="400", height="200")
    op = IntVar()
    # Texto previo a las opciones básicas
    Label(shutdownWindow, text="Por favor seleccione una opción: ").pack()
    # Opciones básicas, se debe elegir una u otra pero no ambas

    shutdown_all = Radiobutton(shutdownWindow, text="Apagar todos los dispositivos/hosts", variable=op, value=1,
                             command=lambda: disabled(checkBtns))
    shutdown_single = Radiobutton(shutdownWindow, text="Apagar un dispositivo/host concreto", variable=op, value=2,
                                command=lambda: enabled(checkBtns))

    shutdown_all.pack()
    shutdown_single.pack()

    # Acción correspondiente a la opción escogida en el menú principal que se le pasará al controlador
    accion = "Apagar"

    # Obtenemos el JSON(diccionario) con toda la información referente a nuestros dispositivos.
    diccionario = getDevices()
    diccionario_hosts = getHosts()

    # Se crea una lista compuesta de texto y una scrollbar(barra) vertical
    lista = Frame(shutdownWindow)
    scrollbar = Scrollbar(lista)
    scrollbar.pack(side=RIGHT, fill=Y, pady=20)

    checklist = Text(lista, height=20, width=15)

    # Se generan los botones Check en base a la cantidad de dispositivos que haya en nuestro diccionario.
    variables_devices = []
    # variables_hosts = []
    v = 0
    i = 1
    c = 0
    checkBtns = []
    ids_devices = []
    # ids_hosts = []
    for check in diccionario.get("devices"):
        variables_devices.append(check.get("id"))
        variables_devices[v] = IntVar()
        v += 1
        ids_devices.append(check.get("id"))
        checkBtns.append(
            Checkbutton(checklist, text=check.get("name"), variable=variables_devices[c], onvalue=i, state=DISABLED))
        checklist.window_create("end", window=checkBtns[c])
        checklist.insert("end", "\n")
        print(variables_devices[c].get())
        i += 1
        c += 1

    for check in diccionario_hosts.get("hosts"):
        variables_devices.append(check.get("id"))
        variables_devices[v] = IntVar()
        v += 1

        ids_devices.append(check.get("id"))
        checkBtns.append(
            Checkbutton(checklist, text=check.get("name"), variable=variables_devices[c], onvalue=i, state=DISABLED))
        checklist.window_create("end", window=checkBtns[c])
        checklist.insert("end", "\n")
        print(variables_devices[c].get())
        i += 1
        c += 1

    checklist.pack(pady=20)
    checklist.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=checklist.yview)

    # disable the widget so users can't insert text into it
    checklist.configure(state="disabled")


    # Botón de confirmación que pasa a la función controller 3 argumentos (la acción (Apagar), la operación deseada y los valores de los checks en ID
    btnConfirmation = Button(shutdownWindow, text="Confirmar acción",
                             command=lambda: [controller(accion, getOpValues(op.get()), getCheckValuesDevices(variables_devices, ids_devices, op.get())), shutdownWindow.destroy()])
    btnConfirmation.pack(pady=20)
    lista.pack()
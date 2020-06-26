from GUIController import controller
from GUImethods import *

def reinicio(raiz):
    rebootWindow = Toplevel(raiz)
    rebootWindow.title("Reiniciar Dispositivos")
    rebootWindow.wm_resizable(0, 0)
    rebootWindow.geometry("400x300")
    op = IntVar()

    #Texto previo a las opciones básicas

    Label(rebootWindow, text="Por favor seleccione una opción: ").pack()

    #Opciones básicas, se debe elegir una u otra pero no ambas

    Reboot_all = Radiobutton(rebootWindow, text="Reiniciar todos los dispositivos", variable=op, value=1, command=lambda: disabled(checkBtns))
    Reboot_single = Radiobutton(rebootWindow, text="Reiniciar un dispositivo concreto", variable=op, value=2, command=lambda: enabled(checkBtns))
    Reboot_single_host = Radiobutton(rebootWindow, text="Reiniciar un host concreto", variable=op, value=3, command=lambda: enabled(checkBtns))

    Reboot_all.pack()
    Reboot_single.pack()
    Reboot_single_host.pack()

    #Acción correspondiente a la opción escogida en el menú principal que se le pasará al controlador
    accion = "Reiniciar"

    # Obtenemos el JSON(diccionario) con toda la información referente a nuestros dispositivos.
    diccionario = getDevices()
    diccionario_hosts = getHosts()


    # Se crea una lista compuesta de texto y una scrollbar(barra) vertical
    lista = Frame(rebootWindow)
    scrollbar = Scrollbar(lista)
    scrollbar.pack(side=RIGHT, fill=Y, pady=20)

    checklist = Text(lista, height=20, width=15)

    # Se generan los botones Check en base a la cantidad de dispositivos que haya en nuestro diccionario.
    variables_devices = []
    #variables_hosts = []
    v = 0
    i = 1
    c = 0
    checkBtns = []
    ids_devices = []
    #ids_hosts = []
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

    # Botón de confirmación que pasa a la función controller 3 argumentos (la acción (Reiniciar), la operación deseada y los valores de los checks en ID
    btnConfirmation = Button(rebootWindow, text="Confirmar acción", command=lambda: [controller(accion, getOpValues(op.get()),
                                                                                                getCheckValuesDevices(variables_devices, ids_devices, op.get())), rebootWindow.destroy()])
    btnConfirmation.pack(pady=20)
    lista.pack()


    print("He pasado el btnConfirmatiao")
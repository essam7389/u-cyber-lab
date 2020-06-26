from GUIController import controller
from GUImethods import *
from tkinter.filedialog import askopenfile

def reseteo(raiz):
    resetWindow = Toplevel(raiz)
    resetWindow.title("Resetear Dispositivos")
    resetWindow.wm_resizable(0, 0)
    resetWindow.geometry("400x250")

    op = IntVar()

    #Texto previo a las opciones básicas
    Label(resetWindow, text="Por favor seleccione una opción: ").pack()

    #Opciones básicas, se debe elegir una u otra pero no ambas
    Reboot_all = Radiobutton(resetWindow, text="Resetear todos los dispositivos", variable=op, value=1, command=lambda: disabled(checkBtns))
    Reboot_single = Radiobutton(resetWindow, text="Resetear un dispositivo concreto", variable=op, value=2, command=lambda: enabled(checkBtns))

    Reboot_all.pack()
    Reboot_single.pack()

    # Acción correspondiente a la opción escogida en el menú principal que se le pasará al controlador
    accion="Resetear"

    # Obtenemos el JSON(diccionario) con toda la información referente a nuestros dispositivos.
    diccionario = getDevices()

    # Se crea una lista compuesta de texto y una scrollbar(barra) vertical
    lista = Frame(resetWindow)
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

    checklist.pack(pady=20)
    checklist.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=checklist.yview)

    # disable the widget so users can't insert text into it
    checklist.configure(state="disabled")

    #Obtenemos un nº concreto de 'files'(archivos de backups) en base a la cantidad de dispositivos que queramos resetear.
    def getFiles(variables_devices, op, ids_devices):
        x = 0
        numDevices = i
        files = []
        lista = []
        if(getOpValues(op) == 1):
            for x in numDevices:
                file = open_file()
                files.append(file)
        else:
            print("HE ENTRADO EN EL ELSE")
            lista = getCheckValuesDevices(variables_devices, ids_devices, op)
            print(lista)

            print(ids_devices)
            print(variables_devices)
            for x in lista:
                if(x != "cero"):
                    file = open_file()
                    files.append(file)
        return files

    #Se abre una ventana donde el usuario selecciona el archivo(backup) que desea cargar y se guarda en la variable 'file'
    def open_file():
        file = askopenfile(mode='r', filetypes=[('Python Files', '*')])
        return file
    print("op.get() = " , op.get())

    btnConfirmation = Button(resetWindow, text="Confirmar acción", command=lambda: [controller(accion, getOpValues(op.get()), getCheckValuesDevices(variables_devices, ids_devices, op.get()), raiz, rutas=getFiles(variables_devices, op.get(), ids_devices)), resetWindow.destroy()])
    btnConfirmation.pack(pady=20)
    lista.pack()

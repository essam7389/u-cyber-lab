from GUIControllerAttack import controller
from GUImethods import *

def scan(raiz):
    '''
    :param raiz: Recibe una dirección a la interfáz gráfica principal de la aplicación
    :return: No devuelve nada
    '''

    stateWindow = Toplevel(raiz)
    stateWindow.title("Escanear Dispositivos")
    stateWindow.wm_resizable(0, 0)
    stateWindow.geometry("400x450")

    op = IntVar()
    # Texto previo a las opciones básicas
    Label(stateWindow, text="Por favor seleccione una opción: ").pack(pady=10)

    # Opciones básicas, se debe elegir una u otra pero no ambas

    scan_all = Radiobutton(stateWindow, text="Escanear todos los hosts", variable=op, value=1,
                                command=lambda: disabled(checkBtns))
    scan_single = Radiobutton(stateWindow, text="Escanear una serie de hosts", variable=op, value=2,
                                   command=lambda: enabled(checkBtns))

    scan_all.pack()
    scan_single.pack()
    # Acción correspondiente a la opción escogida en el menú principal que se le pasará al controlador
    accion = "Scan"
    Redes = []
    Mascaras = []

    # Se pide introducir la red a la cuál se quiere realizar el escaneo
    #label = Frame(stateWindow)
    Lred = Label(stateWindow, text="Introduzca la red a escanear")
    Red = Entry(stateWindow)
    reg = Red.register(comprobarIP)
    Red.config(validate="focusout", validatecommand=(reg, "%s"))
    Redes.append(Red)




    # Se pide introducir el prefijo de red (máscara de subred) de la red a la cuál se quiere realizar el escaneo
    #LMask = Label(label, text="Introduzca el prefijo de subred de la red a escanear")
    Lmask = Label(stateWindow, text="Introduzca el prefijo de subred de la red a escanear")
    Mask = Spinbox(stateWindow, from_=8, to=30)
    Mascaras.append(Mask)

    #Obtenemos el JSON(diccionario) con toda la información referente a nuestros dispositivos.
    diccionario_atacantes = getAttackHosts()

    # Se crea una lista compuesta de texto y una scrollbar(barra) vertical para los clientes
    lista_atacantes = Frame(stateWindow)
    scrollbar_atacantes = Scrollbar(lista_atacantes)
    scrollbar_atacantes.pack(side=RIGHT, fill=Y, pady=20)

    checklistAtacantes = Text(lista_atacantes, height=20, width=15)


    # Se generan los botones Check en base a la cantidad de dispositivos que haya en nuestro diccionario.
    variables_atacantes = []
    v = 0
    i = 1
    c = 0
    checkBtns = []
    ids_atacantes = []

    #Se realiza un bucle que recorrerá todos y cada uno de los dispositivos registrados en el diccionario
    #generándose los checkbuttons para cada uno de ellos
    for atacante_check in diccionario_atacantes.get("hosts"):
        print("Clientes_check: ")
        print(atacante_check)
        variables_atacantes.append(atacante_check.get("id"))
        variables_atacantes[v] = IntVar()
        v += 1
        ids_atacantes.append(atacante_check.get("id"))
        checkBtns.append(
            Checkbutton(checklistAtacantes, text=atacante_check.get("name"), variable=variables_atacantes[c], onvalue=i, state=DISABLED))
        checklistAtacantes.window_create("end", window=checkBtns[c])
        checklistAtacantes.insert("end", "\n")
        #print(variables_clientes[c].get())
        i += 1
        c += 1

    checklistAtacantes.pack(pady=20)
    checklistAtacantes.config(yscrollcommand=scrollbar_atacantes.set)
    scrollbar_atacantes.config(command=checklistAtacantes.yview)

    # Desactiva el widget para que los usuarios no puedan introducir texto
    checklistAtacantes.configure(state="disabled")

    print("HE TERMINADO EL BUCLE")

    # Botón de confirmación que pasa a la función controller 3 argumentos (la acción (Scan), la operación deseada y los valores de los checks en ID
    btnConfirmation = Button(stateWindow, text="Confirmar acción", command=lambda: [
        controller(accion, getOpValues(op.get()), hosts_origen=getCheckValuesDevices(variables_atacantes, ids_atacantes, op.get()), hosts_destino=getIP(Redes), mask=getMask(Mascaras),
                  GUI= raiz), stateWindow.destroy()])
    Lred.pack(pady=15)
    Red.pack(pady=4)
    Lmask.pack(pady=8)
    Mask.pack(pady=4)

    btnConfirmation.pack()
    btnConfirmation.pack(pady=20)
    lista_atacantes.pack()
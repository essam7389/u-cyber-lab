from GUIControllerAttack import controller
from GUImethods import *

def sshAttack(raiz):
    stateWindow = Toplevel(raiz)
    stateWindow.title("Escanear Dispositivos")
    stateWindow.wm_resizable(0, 0)
    stateWindow.geometry("400x500")

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
    accion = "SSHAttack"

    # Se pide introducir la red a la cuál se quiere realizar el SSHAttack
    Redes = []
    Lred = Label(stateWindow, text="Introduzca la red a escanear")
    Red = Entry(stateWindow)
    reg = Red.register(comprobarIP)
    Red.config(validate="focusout", validatecommand=(reg, "%s"))
    Redes.append(Red)

    #Red opcional 1
    Lred1 = Label(stateWindow, text="Introduzca una segunda red alternativa")
    Red1 = Entry(stateWindow)
    reg = Red.register(comprobarIP)
    Red1.config(validate="focusout", validatecommand=(reg, "%s"))
    Redes.append(Red1)

    #Red opcional 2
    Lred2 = Label(stateWindow, text="Introduzca una tercera red alternativa")
    Red2 = Entry(stateWindow)
    reg = Red.register(comprobarIP)
    Red2.config(validate="focusout", validatecommand=(reg, "%s"))
    Redes.append(Red2)

    # Obtenemos el JSON(diccionario) con toda la información referente a nuestros dispositivos.
    diccionario_clientes = getClientHosts()

    # Se crea una lista compuesta de texto y una scrollbar(barra) vertical para los clientes
    lista_clientes = Frame(stateWindow)
    scrollbar_clientes = Scrollbar(lista_clientes)
    scrollbar_clientes.pack(side=RIGHT, fill=Y, pady=20)

    checklistClientes = Text(lista_clientes, height=20, width=15)

    # Se generan los botones Check en base a la cantidad de dispositivos que haya en nuestro diccionario.
    variables_clientes = []
    v = 0
    i = 1
    c = 0
    checkBtns = []
    ids_clientes = []

    # Se realiza un bucle que recorrerá todos y cada uno de los dispositivos registrados en el diccionario
    # generándose los checkbuttons para cada uno de ellos
    for clientes_check in diccionario_clientes.get("hosts"):
        print("Clientes_check: ")
        print(clientes_check)
        variables_clientes.append(clientes_check.get("id"))
        variables_clientes[v] = IntVar()
        v += 1
        ids_clientes.append(clientes_check.get("id"))
        checkBtns.append(
            Checkbutton(checklistClientes, text=clientes_check.get("name"), variable=variables_clientes[c], onvalue=i,
                        state=DISABLED))
        checklistClientes.window_create("end", window=checkBtns[c])
        checklistClientes.insert("end", "\n")
        # print(variables_clientes[c].get())
        i += 1
        c += 1

    checklistClientes.pack(pady=20)
    checklistClientes.config(yscrollcommand=scrollbar_clientes.set)
    scrollbar_clientes.config(command=checklistClientes.yview)

    # Desactiva el widget para que los usuarios no puedan introducir texto
    checklistClientes.configure(state="disabled")

    print("HE TERMINADO EL BUCLE")

    # Botón de confirmación que pasa a la función controller 3 argumentos (la acción (Consultar), la operación deseada y los valores de los checks en ID
    btnConfirmation = Button(stateWindow, text="Confirmar Ataque", command=lambda: [
        controller(accion, getOpValues(op.get()), getCheckValuesDevices(variables_clientes, ids_clientes, op.get()),
                   Redes,
                   raiz), stateWindow.destroy()])
    Lred.pack(pady=15)
    Red.pack(pady=4)

    Lred1.pack(pady=8)
    Red1.pack(pady=4)

    Lred2.pack(pady=8)
    Red2.pack(pady=4)


    btnConfirmation.pack()
    btnConfirmation.pack(pady=20)
    lista_clientes.pack()
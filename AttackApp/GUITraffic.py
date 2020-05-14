from GUIControllerAttack import controller
from GUImethods import *

def generateTraffic(raiz):
    stateWindow = Toplevel(raiz)
    stateWindow.title("Escanear Dispositivos")
    stateWindow.wm_resizable(0, 0)
    stateWindow.geometry("400x350")

    op = IntVar()
    # Texto previo a las opciones básicas
    Label(stateWindow, text="Por favor seleccione una opción: ").pack()

    # Opciones básicas, se debe elegir una u otra pero no ambas

    consultar_all = Radiobutton(stateWindow, text="Escanear todos los hosts", variable=op, value=1,
                                command=lambda: disabled(checkBtns))
    consultar_single = Radiobutton(stateWindow, text="Escanear una serie de hosts", variable=op, value=2,
                                   command=lambda: enabled(checkBtns))

    consultar_all.pack()
    consultar_single.pack()
    # Acción correspondiente a la opción escogida en el menú principal que se le pasará al controlador
    accion = "Scan"

    # Obtenemos el JSON(diccionario) con toda la información referente a nuestros dispositivos.
    diccionario_clientes = getClientHosts()
    diccionario_servidores = getServerHosts()

    # Se crea una lista compuesta de texto y una scrollbar(barra) vertical para los clientes
    lista_clientes = Frame(stateWindow)
    scrollbar_clientes = Scrollbar(lista_clientes)
    scrollbar_clientes.pack(side=RIGHT, fill=Y, pady=20)

    checklistClientes = Text(lista_clientes, height=20, width=15)

    # Se crea una lista compuesta de texto y una scrollbar(barra) vertical para los servidores
    lista_servidor = Frame(stateWindow)
    scrollbar_servidor = Scrollbar(lista_servidor)
    scrollbar_servidor.pack(side=RIGHT, fill=Y, pady=20)

    checklistservidor = Text(lista_servidor, height=20, width=15)

    # Se generan los botones Check en base a la cantidad de dispositivos que haya en nuestro diccionario.
    variables_clientes = []
    variables_servidores = []
    # v = 0
    i = 1
    c = 0
    s = 0
    checkBtns = []
    ids_clientes = []
    ids_servidores = []

    # Se realiza un bucle que recorrerá todos y cada uno de los dispositivos registrados en el diccionario
    # generándose los checkbuttons para cada uno de ellos
    for clientes_check in diccionario_clientes.get("hosts"):
        variables_clientes.append(clientes_check.get("id"))
        variables_clientes.append(IntVar())
        # v += 1
        ids_clientes.append(clientes_check.get("id"))
        checkBtns.append(
            Checkbutton(checklistClientes, text=clientes_check.get("name"), variable=variables_clientes[c], onvalue=i,
                        state=DISABLED))
        checklistClientes.window_create("end", window=checkBtns[c])
        checklistClientes.insert("end", "\n")
        print(variables_clientes[c].get())
        i += 1
        c += 1

    i = 0

    for servidores_check in diccionario_servidores.get("hosts"):
        variables_servidores.append(servidores_check.get("id"))
        variables_servidores.append(IntVar())

        ids_servidores.append(servidores_check.get("id"))
        checkBtns.append(
            Checkbutton(checklistservidor, text=servidores_check.get("name"), variable=variables_servidores[s],
                        onvalue=i, state=DISABLED))
        checklistservidor.window_create("end", window=checkBtns[s])
        checklistservidor.insert("end", "\n")
        print(variables_servidores[s].get())
        i += 1
        s += 1

    checklistClientes.pack(pady=20)
    checklistClientes.config(yscrollcommand=scrollbar_clientes.set)
    scrollbar_clientes.config(command=checklistClientes.yview)

    checklistservidor.pack(pady=20)
    checklistservidor.config(yscrollcommand=scrollbar_servidor.set)
    scrollbar_servidor.config(command=checklistservidor.yview)

    # Desactiva el widget para que los usuarios no puedan introducir texto
    checklistClientes.configure(state="disabled")
    checklistservidor.configure(state="disabled")

    print("HE TERMINADO EL BUCLE")

    # Botón de confirmación que pasa a la función controller 3 argumentos (la acción (Consultar), la operación deseada y los valores de los checks en ID
    btnConfirmation = Button(stateWindow, text="Confirmar acción", command=lambda: [
        controller(accion, getOpValues(op.get()), getCheckValuesDevices(variables_clientes, ids_clientes, op.get()),
                   getCheckValuesDevices(variables_servidores, ids_servidores, op.get()),
                   raiz), stateWindow.destroy()])
    btnConfirmation.pack()
    btnConfirmation.pack(pady=20)
    lista_clientes.pack()
    lista_servidor.pack()
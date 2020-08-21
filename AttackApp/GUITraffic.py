from GUIControllerAttack import controller
from GUImethods import *

def generateTraffic(raiz):
    trafficWindow = Toplevel(raiz)
    trafficWindow.title("Activar/Desactivar Tráfico")
    trafficWindow.wm_resizable(0, 0)
    trafficWindow.geometry("350x350")
    icono = PhotoImage(file='attackIcon.png')
    trafficWindow.iconphoto(False, icono)

    op = IntVar()
    # Texto previo a las opciones básicas
    Label(trafficWindow, text="Por favor seleccione una opción: ").pack()

    # Opciones básicas, se debe elegir una u otra pero no ambas

    consultar_all = Radiobutton(trafficWindow, text="Activar tráfico desde todos los hosts a todos los hosts", variable=op, value=1,
                                command=lambda: [disabled(checkBtnsCliente), disabled(checkBtnsServidor)])
    consultar_single = Radiobutton(trafficWindow, text="Activar tráfico desde hosts concretos a hosts concretos", variable=op, value=2,
                                   command=lambda: [enabled(checkBtnsCliente), enabled(checkBtnsServidor)])

    consultar_all.pack()
    consultar_single.pack()
    # Acción correspondiente a la opción escogida en el menú principal que se le pasará al controlador
    accion = "TrafficFlow"

    # Obtenemos el JSON(diccionario) con toda la información referente a nuestros servidores.
    diccionario = getServerHosts()
    diccionario_clientes = getClientHosts()

    # Se crea una lista compuesta de texto y una scrollbar(barra) vertical
    lista_cliente = Frame(trafficWindow)
    scrollbar_cliente = Scrollbar(lista_cliente)
    scrollbar_cliente.pack(side=RIGHT, fill=Y, pady=20)
    checklistCliente = Text(lista_cliente, height=20, width=15)


    #Se crea una lista para el servidor compuesta de texto y una scrollbar(barra) vertical
    lista_servidor = Frame(trafficWindow)
    scrollbar_servidor = Scrollbar(lista_servidor)
    scrollbar_servidor.pack(side=RIGHT, fill=Y, pady=20)
    checklistServidor = Text(lista_servidor, height=20, width=15)

    # Se generan los botones Check en base a la cantidad de dispositivos que haya en nuestro diccionario.
    variables_servidor = []
    variables_cliente = []
    v = 0
    i = 1
    c = 0
    checkBtnsCliente = []
    checkBtnsServidor = []

    ids_servidor = []
    ids_cliente = []
    # Bucle que obtiene los hosts de tipo servidor
    for cliente in diccionario_clientes.get("hosts"):
        variables_cliente.append(cliente.get("id"))
        variables_cliente[v] = IntVar()
        v += 1
        ids_cliente.append(cliente.get("id"))
        checkBtnsCliente.append(
            Checkbutton(checklistCliente, text=cliente.get("name"), variable=variables_cliente[c], onvalue=i,
                        state=DISABLED))
        checklistCliente.window_create("end", window=checkBtnsCliente[c])
        checklistCliente.insert("end", "\n")
        print(variables_cliente[c].get())
        i += 1
        c += 1


    v = 0
    i = 1
    c = 0
    # Bucle que obtiene los hosts de tipo servidor
    for servidor in diccionario.get("hosts"):
        variables_servidor.append(servidor.get("id"))
        variables_servidor[v] = IntVar()
        v += 1
        ids_servidor.append(servidor.get("id"))
        checkBtnsServidor.append(
            Checkbutton(checklistServidor, text=servidor.get("name"), variable=variables_servidor[c], onvalue=i,
                        state=DISABLED))
        checklistServidor.window_create("end", window=checkBtnsServidor[c])
        checklistServidor.insert("end", "\n")
        print(variables_servidor[c].get())
        i += 1
        c += 1

    checklistCliente.pack(pady=20)
    checklistCliente.config(yscrollcommand=scrollbar_cliente.set)
    scrollbar_cliente.config(command=checklistCliente.yview)

    checklistServidor.pack(pady=20)
    checklistServidor.config(yscrollcommand=scrollbar_servidor.set)
    scrollbar_servidor.config(command=checklistServidor.yview)

    # disable the widget so users can't insert text into it
    checklistCliente.configure(state="disabled")
    checklistServidor.configure(state="disabled")

    # Botón de confirmación que pasa a la función controller 3 argumentos (la acción (Servidor), la operación deseada y los valores de los checks en ID
    btnActivar = Button(trafficWindow, text="Activar Tráfico", command=lambda: [
        controller(accion, getOpValues(op.get()), hosts_origen=getCheckValuesDevices(variables_cliente, ids_cliente, op.get()),
                   hosts_destino=getCheckValuesDevices(variables_servidor, ids_servidor, op.get()),
                   GUI=raiz), trafficWindow.destroy()])

    # Botón de confirmación que pasa a la función controller 3 argumentos (la acción (Servidor), la operación deseada y los valores de los checks en ID
    # y además una suboperacion que en este caso corresponde a la desactivación(--s)
    btnDesactivar = Button(trafficWindow, text="Desactivar Tráfico", command=lambda: [
        controller(accion, getOpValues(op.get()), hosts_origen= getCheckValuesDevices(variables_cliente, ids_cliente, op.get()),
                   hosts_destino=getCheckValuesDevices(variables_servidor, ids_servidor, op.get()), suboperacion="--s",
                   GUI=raiz), trafficWindow.destroy()])

    btnActivar.pack(pady=10, padx=10, side=BOTTOM)
    btnDesactivar.pack(pady=10, padx=10, side=BOTTOM)
    lista_cliente.pack(side=LEFT, padx=20)
    lista_servidor.pack(side=LEFT)
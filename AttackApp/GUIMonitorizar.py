from GUIControllerAttack import controller
from GUImethods import *

def monitorizar(raiz):
    '''
    :param raiz: Recibe una dirección a la interfáz gráfica principal de la aplicación
    :return: No devuelve nada
    '''

    stateWindow = Toplevel(raiz)
    stateWindow.title("SSH Attack")
    stateWindow.wm_resizable(0, 0)
    stateWindow.geometry("400x500")

    op = IntVar()
    # Texto previo a las opciones básicas
    Label(stateWindow, text="Por favor seleccione una opción: ").pack(pady=10)

    # Opciones básicas, se debe elegir una u otra pero no ambas

    scan_all = Radiobutton(stateWindow, text="Redireccionar tráfico desde todos los dispositivos",
                           variable=op, value=1,
                           command=lambda: disabled(checkBtns))
    scan_single = Radiobutton(stateWindow, text="Redireccionar tráfico desde uno o varios dispositivos concretos",
                              variable=op, value=2,
                              command=lambda: enabled(checkBtns))

    scan_all.pack()
    scan_single.pack()
    # Acción correspondiente a la opción escogida en el menú principal que se le pasará al controlador
    accion = "Monitorizar"

    # Se pide introducir la dirección del manager al cuál se le va a reenviar mediante netflow los datos de monitorización
    direcciones = []
    LDireccion = Label(stateWindow, text="Introduzca la dirección a la que se enviarán los datos de monitorización")
    Direccion = Entry(stateWindow)
    reg = Direccion.register(comprobarIP)
    Direccion.config(validate="focusout", validatecommand=(reg, "%s"))
    direcciones.append(Direccion)

    # Obtenemos el JSON(diccionario) con toda la información referente a nuestros dispositivos.
    diccionario_devices = getDevices()

    # Se crea una lista compuesta de texto y una scrollbar(barra) vertical para los clientes
    lista_devices = Frame(stateWindow)
    scrollbar_devices = Scrollbar(lista_devices)
    scrollbar_devices.pack(side=RIGHT, fill=Y, pady=20)

    checklistDevices = Text(lista_devices, height=20, width=15)

    # Se generan los botones Check en base a la cantidad de dispositivos que haya en nuestro diccionario.
    variables_devices = []
    v = 0
    i = 1
    c = 0
    checkBtns = []
    ids_devices = []

    # Se realiza un bucle que recorrerá todos y cada uno de los dispositivos registrados en el diccionario
    # generándose los checkbuttons para cada uno de ellos
    for device in diccionario_devices.get("devices"):
        print("Clientes_check: ")
        print(device)
        variables_devices.append(device.get("id"))
        variables_devices[v] = IntVar()
        v += 1
        ids_devices.append(device.get("id"))
        checkBtns.append(
            Checkbutton(checklistDevices, text=device.get("name"), variable=variables_devices[c], onvalue=i,
                        state=DISABLED))
        checklistDevices.window_create("end", window=checkBtns[c])
        checklistDevices.insert("end", "\n")
        # print(variables_clientes[c].get())
        i += 1
        c += 1

    checklistDevices.pack(pady=20)
    checklistDevices.config(yscrollcommand=scrollbar_devices.set)
    scrollbar_devices.config(command=checklistDevices.yview)

    # Desactiva el widget para que los usuarios no puedan introducir texto
    checklistDevices.configure(state="disabled")

    # Botón de confirmación que pasa a la función controller 3 argumentos (la acción (Monitorizar), la operación deseada y los valores de los checks en ID
    btnConfirmation = Button(stateWindow, text="Confirmar acción", command=lambda: [
        controller(accion, getOpValues(op.get()),
                   hosts_origen=getCheckValuesDevices(variables_devices, ids_devices, op.get()),
                   hosts_destino=getIP(direcciones),
                   GUI=raiz), stateWindow.destroy()])
    LDireccion.pack(pady=15)
    Direccion.pack(pady=4)


    btnConfirmation.pack()
    btnConfirmation.pack(pady=20)
    lista_devices.pack()
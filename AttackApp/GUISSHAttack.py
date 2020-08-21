from GUIControllerAttack import *
from GUImethods import *

def sshAttack(raiz):
    '''
    :param raiz: Se recibe la dirección de memoría de la interfáz gráfica de Tkinter
    :return: No se devuelve nada, simplemente se llama a la función 'Controller' definida en 'GUIControllerAttack.py'
    '''
    attackWindow = Toplevel(raiz)
    attackWindow.title("SSH Attack")
    attackWindow.wm_resizable(0, 0)
    attackWindow.geometry("400x500")
    icono = PhotoImage(file='attackIcon.png')
    attackWindow.iconphoto(False, icono)

    op = IntVar()
    # Texto previo a las opciones básicas
    Label(attackWindow, text="Por favor seleccione una opción: ").pack(pady=10)

    # Opciones básicas, se debe elegir una u otra pero no ambas

    scan_all = Radiobutton(attackWindow, text="Atacar desde todos los hosts atacantes a los objetivos seleccionados", variable=op, value=1,
                           command=lambda: disabled(checkBtns))
    scan_single = Radiobutton(attackWindow, text="Atacar desde un host concreto a los objetivos seleccionados", variable=op, value=2,
                              command=lambda: enabled(checkBtns))

    scan_all.pack()
    scan_single.pack()
    # Acción correspondiente a la opción escogida en el menú principal que se le pasará al controlador
    accion = "SSHAttack"

    # Se pide introducir la red a la cuál se quiere realizar el SSHAttack
    Redes = []
    Lred = Label(attackWindow, text="Introduzca la red a atacar")
    Red = Entry(attackWindow)
    reg = Red.register(comprobarIP)
    Red.config(validate="focusout", validatecommand=(reg, "%s"))
    print("reg = " + reg)
    print("red.get() = ", Red.get())
    Redes.append(Red)

    #Red opcional 1
    Lred1 = Label(attackWindow, text="Introduzca una segunda red alternativa")
    Red1 = Entry(attackWindow)
    Red1.insert(0, "")
    reg1 = Red1.register(comprobarIP)
    Red1.config(validate="focusout", validatecommand=(reg1, "%s"))

    Redes.append(Red1)

    #Red opcional 2
    Lred2 = Label(attackWindow, text="Introduzca una tercera red alternativa")
    Red2 = Entry(attackWindow)

    reg2 = Red2.register(comprobarIP)

    Red2.config(validate="focusout", validatecommand=(reg2, "%s"))
    Redes.append(Red2)

    # Obtenemos el JSON(diccionario) con toda la información referente a nuestros dispositivos.
    diccionario_atacantes = getAttackHosts()

    # Se crea una lista compuesta de texto y una scrollbar(barra) vertical para los clientes
    lista_atacantes = Frame(attackWindow)
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

    # Se realiza un bucle que recorrerá todos y cada uno de los dispositivos registrados en el diccionario
    # generándose los checkbuttons para cada uno de ellos
    for atacante_check in diccionario_atacantes.get("hosts"):
        print("Clientes_check: ")
        print(atacante_check)
        variables_atacantes.append(atacante_check.get("id"))
        variables_atacantes[v] = IntVar()
        v += 1
        ids_atacantes.append(atacante_check.get("id"))
        checkBtns.append(
            Checkbutton(checklistAtacantes, text=atacante_check.get("name"), variable=variables_atacantes[c], onvalue=i,
                        state=DISABLED))
        checklistAtacantes.window_create("end", window=checkBtns[c])
        checklistAtacantes.insert("end", "\n")
        # print(variables_clientes[c].get())
        i += 1
        c += 1

    checklistAtacantes.pack(pady=20)
    checklistAtacantes.config(yscrollcommand=scrollbar_atacantes.set)
    scrollbar_atacantes.config(command=checklistAtacantes.yview)

    # Desactiva el widget para que los usuarios no puedan introducir texto
    checklistAtacantes.configure(state="disabled")

    # Botón de confirmación que pasa a la función controller 3 argumentos (la acción (SSHAttack), la operación deseada y los valores de los checks en ID
    btnConfirmation = Button(attackWindow, text="Confirmar acción", command=lambda: [
        controller(accion, getOpValues(op.get()),
                   hosts_origen=getCheckValuesDevices(variables_atacantes, ids_atacantes, op.get()),
                   hosts_destino=getIP(Redes),
                   GUI=raiz), print(Redes[0]), attackWindow.destroy()])

    #Se incluyen los widgets de entrada y los botones
    Lred.pack(pady=15)
    Red.pack(pady=4)

    Lred1.pack(pady=8)
    Red1.pack(pady=4)

    Lred2.pack(pady=8)
    Red2.pack(pady=4)

    btnConfirmation.pack()
    btnConfirmation.pack(pady=20)
    lista_atacantes.pack()
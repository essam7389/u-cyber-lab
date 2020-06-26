from GUImethods import *
from addDiccinario import *

def addDiccionario(raiz):
    '''
    :param raiz: Se recibe la dirección de memoría de la interfáz gráfica de Tkinter
    :return: No se devuelve nada, simplemente se llama a la función 'Controller' definida en 'GUIControllerAttack.py'
    '''
    
    addWindow = Toplevel(raiz)
    addWindow.title("SSH Attack")
    addWindow.wm_resizable(0, 0)
    addWindow.geometry("400x1000")

    op = IntVar()
    # Texto previo a las opciones básicas
    Label(addWindow, text="Por favor complete todos los campos para añadir un nuevo dispositivo:").pack(pady=10)

    # Opciones básicas, se debe elegir una u otra pero no ambas

    scan_all = Radiobutton(addWindow, text="Añadir dispositivo",
                           variable=op, value=1,
                           command=lambda: disabled(entryBtns))
    scan_single = Radiobutton(addWindow, text="Añadir host",
                              variable=op, value=2,
                              command=lambda: enabled(entryBtns))

    scan_all.pack()
    scan_single.pack()

    # Se crea una lista compuesta de texto y una scrollbar(barra) vertical para los clientes
    lista_entrys = Frame(addWindow)
    scrollbar = Scrollbar(lista_entrys)
    Entrys = Text(lista_entrys, height=20, width=15)
    scrollbar.pack(side=RIGHT, fill=Y, pady=20)
    Entrys.pack(pady=20)

    # Se crean las cajas de texto donde se introducirá la información correspondiente al dispositivo o host
    labelUsuario = Label(Entrys, text="Introduzca el nombre de usuario para acceder al dispositivo o host")
    usuario = Entry(Entrys)
    Entrys.window_create("end", window=labelUsuario)
    Entrys.insert("end", "\n")
    Entrys.window_create("end", window=usuario)
    Entrys.insert("end", "\n")

    labelContrasenna = Label(Entrys, text="Introduzca la contraseña para acceder al dispositivo o host")
    contrasenna = Entry(Entrys)
    Entrys.window_create("end", window=labelContrasenna)
    Entrys.insert("end", "\n")
    Entrys.window_create("end", window=contrasenna)
    Entrys.insert("end", "\n")

    labelPuerto = Label(Entrys, text="Introduzca el puerto para acceder al dispositivo o host")
    puerto = Spinbox(Entrys, from_=1, to=65990)
    Entrys.window_create("end", window=labelPuerto)
    Entrys.insert("end", "\n")
    Entrys.window_create("end", window=puerto)
    Entrys.insert("end", "\n")

    labelDescripcion = Label(Entrys, text="Introduzca la descripción del dispositivo o host")
    descripcion = Entry(Entrys)
    Entrys.window_create("end", window=labelDescripcion)
    Entrys.insert("end", "\n")
    Entrys.window_create("end", window=descripcion)
    Entrys.insert("end", "\n")

    labelID= Label(Entrys, text="Introduzca el ID del dispositivo o host")
    id = Entry(Entrys)
    Entrys.window_create("end", window=labelID)
    Entrys.insert("end", "\n")
    Entrys.window_create("end", window=id)
    Entrys.insert("end", "\n")

    labelIpmanagement = Label(Entrys, text="Introduzca la ip correspondiente a la red de gestión")
    ip_management = Entry(Entrys)
    Entrys.window_create("end", window=labelIpmanagement)
    Entrys.insert("end", "\n")
    Entrys.window_create("end", window=ip_management)
    Entrys.insert("end", "\n")

    labelIpdatos = Label(Entrys, text="Introduzca la ip correspondiente a la red de datos")
    ip_data = Entry(Entrys)
    Entrys.window_create("end", window=labelIpdatos)
    Entrys.insert("end", "\n")
    Entrys.window_create("end", window=ip_data)
    Entrys.insert("end", "\n")

    #A partir de de aquí los campos son únicamente para los hosts

    entryBtns = []

    labelTeam = Label(Entrys, text="Introduzca el team correspondiente al host")
    team = Entry(Entrys)
    Entrys.window_create("end", window=labelTeam)
    Entrys.insert("end", "\n")
    Entrys.window_create("end", window=team)
    Entrys.insert("end", "\n")
    entryBtns.append(team)


    labelTipo = Label(Entrys, text="Introduzca el tipo de host ")
    tipo = Entry(Entrys)
    Entrys.window_create("end", window=labelTipo)
    Entrys.insert("end", "\n")
    Entrys.window_create("end", window=tipo)
    Entrys.insert("end", "\n")
    entryBtns.append(tipo)

    labelSo = Label(Entrys, text="Introduzca el sistema operativo que tiene el host")
    so = Entry(Entrys)
    Entrys.window_create("end", window=labelSo)
    Entrys.insert("end", "\n")
    Entrys.window_create("end", window=so)
    Entrys.insert("end", "\n")
    entryBtns.append(so)

    # Desactiva el widget para que los usuarios no puedan introducir texto
    Entrys.configure(state="disabled")

    # Obtenemos el JSON(diccionario) con toda la información referente a nuestros dispositivos.


    #Botón de confirmación que pasa a la función controller 3 argumentos (la acción (Scan), la operación deseada y los valores de los checks en ID
    btnConfirmation = Button(addWindow, text="Confirmar acción", command=lambda: [
        mensajePregunta("¿Está seguro de añadir el dispositivo/host al diccionario?", "Confirmar añadido")])

    # Se incluyen los widgets de entrada y los botones
    labelUsuario.pack(pady=15)
    usuario.pack(pady=4)

    labelContrasenna.pack(pady=15)
    contrasenna.pack(pady=4)

    labelPuerto.pack(pady=15)
    puerto.pack(pady=4)

    labelDescripcion.pack(pady=15)
    descripcion.pack(pady=4)

    labelID.pack(pady=15)
    id.pack(pady=4)

    labelIpmanagement.pack(pady=15)
    ip_management.pack(pady=4)

    labelIpdatos.pack(pady=15)
    ip_data.pack(pady=4)

    labelTeam.pack(pady=15)
    team.pack(pady=4)

    labelTipo.pack(pady=15)
    tipo.pack(pady=4)

    labelSo.pack(pady=15)
    so.pack(pady=4)

    Entrys.pack(pady=20)
    Entrys.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=Entrys.yview)

    btnConfirmation.pack()
    btnConfirmation.pack(pady=20)

    lista_entrys.pack()


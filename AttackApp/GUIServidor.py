from GUIControllerAttack import controller
from GUImethods import *

def servers(raiz):
    stateWindow = Toplevel(raiz)
    stateWindow.title("Activar Servidores")
    stateWindow.wm_resizable(0, 0)
    stateWindow.geometry("400x250")

    op = IntVar()
    # Texto previo a las opciones básicas
    Label(stateWindow, text="Por favor seleccione una opción: ").pack()

    # Opciones básicas, se debe elegir una u otra pero no ambas

    consultar_all = Radiobutton(stateWindow, text="Consultar todos los dispositivos", variable=op, value=1,
                                command=lambda: disabled(checkBtns))
    consultar_single = Radiobutton(stateWindow, text="Consultar un dispositivo concreto", variable=op, value=2,
                                   command=lambda: enabled(checkBtns))

    consultar_all.pack()
    consultar_single.pack()
    # Acción correspondiente a la opción escogida en el menú principal que se le pasará al controlador
    accion = "Servidor"
    subop = ""
    # Obtenemos el JSON(diccionario) con toda la información referente a nuestros servidores.
    diccionario = getServerHosts()

    # Se crea una lista compuesta de texto y una scrollbar(barra) vertical
    lista = Frame(stateWindow)
    scrollbar = Scrollbar(lista)
    scrollbar.pack(side=RIGHT, fill=Y, pady=20)

    checklist = Text(lista, height=20, width=15)

    # Se generan los botones Check en base a la cantidad de dispositivos que haya en nuestro diccionario.
    variables_servidor = []
    v = 0
    i = 1
    c = 0
    checkBtns = []
    ids_servidor = []
    #Bucle que obtiene los hosts de tipo servidor
    for servidor in diccionario.get("hosts"):
        variables_servidor.append(servidor.get("id"))
        variables_servidor[v] = IntVar()
        v += 1
        ids_servidor.append(servidor.get("id"))
        checkBtns.append(
            Checkbutton(checklist, text=servidor.get("name"), variable=variables_servidor[c], onvalue=i, state=DISABLED))
        checklist.window_create("end", window=checkBtns[c])
        checklist.insert("end", "\n")
        print(variables_servidor[c].get())
        i += 1
        c += 1

    checklist.pack(pady=20)
    checklist.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=checklist.yview)

    # disable the widget so users can't insert text into it
    checklist.configure(state="disabled")

    # Botón de confirmación que pasa a la función controller 3 argumentos (la acción (Servidor), la operación deseada y los valores de los checks en ID
    btnActivar = Button(stateWindow, text="Activar Servidor", command=lambda: [
        controller(accion, getOpValues(op.get()), hosts_destino=getCheckValuesDevices(variables_servidor, ids_servidor, op.get()),
                   GUI=raiz), stateWindow.destroy()])

    # Botón de confirmación que pasa a la función controller 3 argumentos (la acción (Servidor), la operación deseada y los valores de los checks en ID
    #y además una suboperacion que en este caso corresponde a la desactivación(--s)
    btnDesactivar = Button(stateWindow, text="Desactivar Servidor", command=lambda: [
        controller(accion, getOpValues(op.get()), hosts_destino=getCheckValuesDevices(variables_servidor, ids_servidor, op.get()), suboperacion="--s",
                   GUI=raiz), stateWindow.destroy()])

    btnActivar.pack(pady=20)
    btnDesactivar.pack(pady=20, side=LEFT)
    lista.pack(side=BOTTOM)
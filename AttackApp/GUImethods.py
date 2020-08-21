from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import messagebox


from JSONmethods import *
import re
# Función que devuelve el tipo de operación según el RadioButtom seleccionado.
# Devuelve "-a" para cuando se selecciona para todos los dispositivos
# Devuelve "-d" para cuando se selecciona para un grupo de dispositivos
def getOpValues(op):
    '''
    :param op: Recibe un tipo de operación como un entero (1 o 2)
    :return: Devuelve el tipo de operación como un string
    '''
    if (op == 1):
        operacion = "-a"
    else:
        operacion = "-d"

    return operacion


# Función para obtener los valores de los checks y en función de ellos asignar un ID de la clase Dispositivo ("SW", "WR"...)
def getCheckValuesDevices(variables, ids, operacion):
    '''
    :param variables: Recibe los valores de los checks
    :param ids: Recibe los ids correspondientes a los dispositivos
    :param operacion: Recibe el tipo de operación como un entero
    :return: Devuelve los nics de los dispositivos que el usuario previamente a seleccionado en la interfáz
    '''
    dispositivos = []
    print(variables)
    #Solo se realiza para cuando la operación elegida es "-d"
    if(operacion == 2):
        id = iter(ids)

        for v in variables:
            nic = id.__next__()
            if(v.get()!=0):
                dispositivos.append(nic)
            else:
                dispositivos.append("cero")

    return dispositivos


def loading(raiz):
    '''
    :param raiz: Recibe una dirección a la interfáz gráfica principal de la aplicación
    :return: No devuelve nada
    '''
    #print("raiz = " .format(raiz))
    progressAttackWindow = Toplevel(raiz)
    progressAttackWindow.title("SSHAttack progreso")
    progressAttackWindow.wm_resizable(0, 0)
    progressAttackWindow.geometry("300x300")
    progressbar = Progressbar(progressAttackWindow)
    progressbar.place(x=30, y=60, width=200)
    progressbar.start(10)
   # print("Salgo de loading")

#def loadingStop(raiz):
    '''
    :param raiz: Recibe una dirección a la interfáz gráfica principal de la aplicación
    :return: No devuelve nada
    '''
    #raiz.progressbar.stop()


def comprobarIP(ip):
    '''
    :param ip: Recibe una ip introducida por el usuario
    :return: Devuelve true si la ip introducida posee el formato de ip, en caso contrario devuelve false
    '''

    exp = "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    print("ip = ", ip)
    if(re.search(exp, str(ip))):
        print("devuelvo true")
        return True

    elif(ip == ""):
        print("devuelvo false con ip vacia")
        return False
    else:
        mensajeError("La ip introducida es errónea", "IP Errónea")
        exit()



def comprobarMascara(mask):
    '''
    :param mask: Recibe una máscara introducida por el usuario
    :return: Devuelve true si la máscara introducida posee el formato de ip, en caso contrario devuelve false
    '''
    exp = "^([0-9]{1,2})$"
    if (re.search(exp, mask)):
        return True
    else:
        return False


def mensajeError(mensaje, titulo):
    '''
    :param mensaje: Se recibe el mensaje de error que se mostrará en la ventana de error
    :param titulo: Se recibe el título a mostrar en la ventana de error de la aplicación
    :return: No se devuelve nada.
    '''
    messagebox.showerror(message=mensaje, title=titulo)


def getIP(lista_ips):
    '''
    :param lista_ips: Se recibe una lista de referencias a ips introducidas por el usuario a través de la interfáz gráfica
    :return: Se devuelve una lista de ips
    '''
    ips = []
    for ip in lista_ips:

        if(comprobarIP(ip.get()) == True):
            ips.append(ip.get())


    return ips
def getMask(mascaras):
    '''
    :param mascaras: Se recibe una lista de referencias a máscaras introducidas por el usuario a través de la interfáz gráfica
    :return: Se devuelve una lista de máscaras
    '''
    masks = []
    for mask in mascaras:
        masks.append(mask.get())

    return masks

'''
# Función para obtener los valores de los checks y en función de ellos asignar un ID de la clase Dispositivo ("SW", "WR"...)
def getCheckValuesHosts(variables, ids, operacion):
    hosts = []
    if (operacion == 3):
        id = iter(ids)

        for v in variables:
            nic = id.__next__()
            if (v.get() != 0):
                hosts.append(nic)
            else:
                hosts.append("cero")

    return hosts
'''



# Función que activa los checks una vez se active la opción de Consultar un dispositivo concreto
def enabled(checkBtns):
    '''
    :param checkBtns: Recibe una lista de direcciones a cada uno de los checksButtoms
    :return: No devuelve nada
    '''
    #Activa los checksButtoms
    for checkBtn in checkBtns:
        checkBtn.config(state=NORMAL)



# Función que desactiva los checks una vez se active la opción de Consultar todos los dispositivos
def disabled(checkBtns):
    '''
    :param checkBtns: Recibe una lista de direcciones a cada uno de los checksButtoms
    :return: No devuelve nada
    '''
    # Desactiva los checkButtoms
    for checkBtn in checkBtns:
        checkBtn.config(state=DISABLED)
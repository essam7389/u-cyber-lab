from tkinter import *
from JSONmethods import *
import re
# Función que devuelve el tipo de operación según el RadioButtom seleccionado.
# Devuelve "-a" para cuando se selecciona para todos los dispositivos
# Devuelve "-d" para cuando se selecciona para un grupo de dispositivos
def getOpValues(op):
    if (op == 1):
        operacion = "-a"
    else:
        operacion = "-d"

    return operacion


# Función para obtener los valores de los checks y en función de ellos asignar un ID de la clase Dispositivo ("SW", "WR"...)
def getCheckValuesDevices(variables, ids, operacion):
    dispositivos = []
    print(variables)
    if(operacion == 2):
        id = iter(ids)

        for v in variables:
            nic = id.__next__()
            if(v.get()!=0):
                dispositivos.append(nic)
            else:
                dispositivos.append("cero")

    return dispositivos



def comprobarIP(ip):
    exp = "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    if(re.search(exp, str(ip))):
        return True

    elif(ip == ""):
        return False
    else:
        mensajeError()
        return False



def comprobarMascara(mask):
    exp = "^([0-9]{1,2})$"
    if (re.search(exp, mask)):
        return True
    else:
        return False


def mensajeError():
    from tkinter import messagebox
    messagebox.showerror(message="Error en el formulario enviado", title="Error de formulario")


def getIP(lista_ips):
    ips = []
    for ip in lista_ips:
        ips.append(ip.get())

    return ips
def getMask(mascaras):
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
    for checkBtn in checkBtns:
        checkBtn.config(state=NORMAL)



# Función que desactiva los checks una vez se active la opción de Consultar todos los dispositivos
def disabled(checkBtns):
    for checkBtn in checkBtns:
        checkBtn.config(state=DISABLED)
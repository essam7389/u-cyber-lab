from tkinter import *
from tkinter import messagebox

from JSONmethods import *

# Función que devuelve el tipo de operación según el RadioButtom seleccionado.
# Devuelve "-a" para cuando se selecciona para todos los dispositivos
# Devuelve "-d" para cuando se selecciona para un grupo de dispositivos
def getOpValues(op):
    '''
    :param op: Recibe un entero que puede ser 1 o distinto, si es 1 se corresponde con la operación '-a' y si no con la '-d'
    :return:
    '''
    if (op == 1):
        operacion = "-a"
    else:
        operacion = "-d"

    return operacion


# Función para obtener los valores de los checks y en función de ellos asignar un ID de la clase Dispositivo ("SW", "WR"...)
def getCheckValuesDevices(variables, ids, operacion):
    '''
    :param variables: Recibe una serie de variables correspondientes a los dispositivos, concretamente nos dicen
    si se ha marcado dicho dispositivo para realizar una determinada acción o no.
    :param ids: Recibe un vector de ids correspondientes a los ids de los dispositivos de los que se quiere obtener
    :param operacion: Recibe un entero que puede ser 2 o distinto, en caso de 2 únicamente se obtendrán los valores
    de los dispositivos cuyo ids aparezcan en el parámetro ids
    :return: Devuelve los dispositivos que cumplen que hayan sido seleccionados por el usuario para realizar una determinada acción
    '''
    dispositivos = []
    print("variables = ",variables)
    print("ids = ", ids)
    print("operacion = ", operacion)
    if(operacion == 2):
        id = iter(ids)

        for v in variables:
            nic = id.__next__()
            if(v.get()!=0):
                dispositivos.append(nic)
            else:
                dispositivos.append("cero")
    print("dispositivos = ", dispositivos)
    return dispositivos



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

def mensajePregunta(mensaje, titulo):
    '''
       :param mensaje: Se recibe el mensaje de confirmación que se mostrará en la ventana de advertencia
       :param titulo: Se recibe el título a mostrar en la ventana de advertencia de la aplicación
       :return: Devuelve true en caso de que se elija Sí y false en caso contrario.
       '''
    return messagebox.askquestion(message=mensaje, title=titulo)


# Función que activa los checks una vez se active la opción de Consultar un dispositivo concreto
def enabled(checkBtns):
    '''
    :param checkBtns: Recibe los check buttoms
    :return: No devuelve nada
    '''
    for checkBtn in checkBtns:
        checkBtn.config(state=NORMAL)



# Función que desactiva los checks una vez se active la opción de Consultar todos los dispositivos
def disabled(checkBtns):
    '''
    :param checkBtns: Recibe los check buttoms
    :return: No devuelve nada
    '''
    for checkBtn in checkBtns:
        checkBtn.config(state=DISABLED)
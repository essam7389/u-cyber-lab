
from addDiccinario import *
from editDiccionario import *
from deleteDiccionario import *


def controllerDiccionario(accion, identificador = None, variables = []):
    usuario = variables[0]
    password = variables[1]
    port = variables[2]
    descripcion = variables[3]
    id = variables[4]
    ip_management = variables[5]
    type_management = variables[6]
    nicname_management = variables[7]
    id_management = variables[8]
    ip_data = variables[9]
    type_data = variables[10]
    nicname_data = variables[11]
    id_data = variables[12]
    team = variables[13]
    tipo_host = variables[14]
    so = variables[15]

    '''if(tipo == "Host"):
        team = variables[13]
        tipo_host = variables[14]
        so = variables[15]
    '''

    if(accion == "Añadir"):

        add(usuario, password, port, descripcion, id, ip_management, type_management,
                nicname_management, id_management, ip_data, type_data, nicname_data, id_data, team, tipo_host, so)


    elif(accion == "Editar"):
        edit(identificador, usuario, password, port, descripcion, id, ip_management, type_management,
            nicname_management, id_management, ip_data, type_data, nicname_data, id_data, team, tipo_host, so)
    elif(accion == "Delete"):
        delete(identificador)
    else:
        print()


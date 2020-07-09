from GUImethods import *

def edit(id_edit, username, password, port, name, description, id, ip_management, type_management, nicname_management, id_management,
        ip_data, type_data, nicname_data, id_data, team_host = None, tipo_host = None, so_host = None):

    if(team_host and tipo_host and so_host):
        editDevices(id_edit, username, password, port, name, description, id, ip_management, type_management, nicname_management,
                   id_management, ip_data, type_data, nicname_data, id_data)

    else:
        editHosts(id_edit, username, password, port, name, description, id, ip_management, type_management, nicname_management,
                   id_management, ip_data, type_data, nicname_data, id_data, team_host, tipo_host, so_host)


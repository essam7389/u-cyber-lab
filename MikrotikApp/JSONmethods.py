import json


def existKey(lista, key):
    for x in lista:
        if(x == key):
            return True

    return False

def addDevices(username, password, port, nombre, description, id, ip_management, type_management, nicname_management, id_management,
        ip_data, type_data, nicname_data, id_data):
    devices = {
        "username": username,
        "password": password,
        "port": port,
        "name": nombre,
        "description": description,
        "id": id,
        "nics": {"management":
             {"IP": ip_management, "type": type_management, "nicname": nicname_management, "id": id_management},
            "data":
             {"IP": ip_data, "type": type_data, "nicname": nicname_data, "id": id_data}
         }
    }

    with open('dispositivos.json', 'w') as file:
        json.dump(devices, file)


def addHosts(username, password, port, nombre, description, id, ip_management, type_management, nicname_management, id_management,
        ip_data, type_data, nicname_data, id_data, team, tipo, so):
    hosts = {
        "username": username,
        "password": password,
        "port": port,
        "name": nombre,
        "description": description,
        "id": id,
        "nics": {"management":
                     {"IP": ip_management, "type": type_management, "nicname": nicname_management, "id": id_management},
                 "data":
                     {"IP": ip_data, "type": type_data, "nicname": nicname_data, "id": id_data}
                 },
        "team": team,
        "tipo": tipo,
        "so": so
    }
    with open('host.json', 'w') as file:
        json.dump(hosts, file['hosts'])

def editDevices(id_edit, username, password, port, nombre, description, id, ip_management, type_management, nicname_management, id_management,
        ip_data, type_data, nicname_data, id_data):
    with open('dispositivos.json') as data_file:
        devices = json.load(data_file)


    # Iterate through the objects in the JSON and pop (remove)
    # the obj once we find it.
    for i in devices['devices']:
        if i['id'] == id_edit:
            i['username'] = username
            i['password'] = password
            i['port'] = port
            i['name'] = nombre
            i['description'] = description
            i['nics']['management']['IP'] = ip_management
            i['nics']['management']['type'] = type_management
            i['nics']['management']['nicname'] = nicname_management
            i['nics']['management']['id'] = id_management

            i['nics']['data']['IP'] = ip_data
            i['nics']['data']['type'] = type_data
            i['nics']['data']['nicname'] = nicname_data
            i['nics']['data']['id'] = id_data


    # Output the updated file with pretty JSON
    open("dispositivos.json", "w").write(
        json.dumps(devices)
    )

def editHosts(id_edit, username, password, port, nombre, description, id, ip_management, type_management, nicname_management, id_management,
              ip_data, type_data, nicname_data, id_data, team, tipo, so):
    # !/usr/bin/python


    # Iterate through the objects in the JSON and pop (remove)
    # the obj once we find it.
    with open('host.json') as data_file:
        hosts = json.load(data_file)


    # Iterate through the objects in the JSON and pop (remove)
    # the obj once we find it.
    for i in hosts['hosts']:
        if i['id'] == id_edit:
            i['username'] = username
            i['password'] = password
            i['port'] = port
            i['name'] = nombre
            i['description'] = description
            i['nics']['management']['IP'] = ip_management
            i['nics']['management']['type'] = type_management
            i['nics']['management']['nicname'] = nicname_management
            i['nics']['management']['id'] = id_management
            i['nics']['data']['IP'] = ip_data
            i['nics']['data']['type'] = type_data
            i['nics']['data']['nicname'] = nicname_data
            i['nics']['data']['id'] = id_data
            i['team'] = team
            i['tipo'] = tipo
            i['so'] = so




    # Output the updated file with pretty JSON
    open("host.json", "w").write(
        json.dumps(hosts)
    )

def deleteDevices(id):
    with open('dispositivos.json') as data_file:
        devices = json.load(data_file)


    # Iterate through the objects in the JSON and pop (remove)
    # the obj once we find it.
    for i in devices['devices']:
        if i['id'] == id:
            del i

    # Output the updated file with pretty JSON
    open("dispositivos.json", "w").write(
        json.dumps(devices)
    )

def deleteHosts(id):
    with open('host.json') as data_file:
        hosts = json.load(data_file)


    # Iterate through the objects in the JSON and pop (remove)
    # the obj once we find it.
    for i in hosts['hosts']:
        if i['id'] == id:
            del i

    # Output the updated file with pretty JSON
    open("host.json", "w").write(
        json.dumps(hosts)
    )

def getDevices():
    with open('Diccionarios\dispositivos.json', 'r') as f:  # Se realiza la lectura del fichero JSON
        direcciones_dict = json.load(f)  # Se guardan los datos del fichero JSON en la variable direcciones_dict que nos permitirá acceder a los diversos campos del JSON
    return (direcciones_dict)


def getHosts():
    with open('Diccionarios\host.json', 'r') as f:  # Se realiza la lectura del fichero JSON
        direcciones_dict = json.load(f)  # Se guardan los datos del fichero JSON en la variable direcciones_dict que nos permitirá acceder a los diversos campos del JSON
    return (direcciones_dict)

def getDevicesBynic(nics):
    direcciones_dict = getDevices()
    #print(direcciones_dict)
    values = []

    print("He entrado en getJsonBynic")
    print(direcciones_dict)
    diccionario = direcciones_dict.fromkeys(direcciones_dict.keys())
    print(diccionario)
    print(nics)

    for i in nics:
        for device in direcciones_dict.get("devices"):
            if(device.get("id")==i):
                values.append({'username': device.get("username"), 'password': device.get("password"), 'port': device.get("port"), 'name': device.get("name"), 'id': device.get("id"),
     'description': device.get("description"), 'nics': device.get("nics")})

    diccionario['devices'] = values
    print("claves del diccionario: ")
    print(diccionario.keys())
    print(diccionario)
    return(diccionario)



def getHostsBynic(nics):
    direcciones_dict = getHosts()
    values = []

    print("He entrado en getJsonBynic")
    print(direcciones_dict)
    diccionario = direcciones_dict.fromkeys(direcciones_dict.keys())
    print(diccionario)
    print(nics)

    for i in nics:
        for host in direcciones_dict.get("hosts"):
            if(host.get("id")==i):
                values.append({'username': host.get("username"), 'password': host.get("password"), 'port': host.get("port"), 'name': host.get("name"), 'id': host.get("id"),
     'description': host.get("description"), 'nics': host.get("nics")})



    diccionario['hosts'] = values
    print("claves del diccionario: ")
    print(diccionario.keys())
    print(diccionario)
    return(diccionario)


import json


def existKey(lista, key):
    for x in lista:
        if(x == key):
            return True

    return False


def getDevices():
    with open('/Diccionarios/dispositivos.json', 'r') as f:  # Se realiza la lectura del fichero JSON
        direcciones_dict = json.load(f)  # Se guardan los datos del fichero JSON en la variable direcciones_dict que nos permitirá acceder a los diversos campos del JSON
    return (direcciones_dict)


def getHosts():
    with open('/Diccionarios/host.json', 'r') as f:  # Se realiza la lectura del fichero JSON
        direcciones_dict = json.load(f)  # Se guardan los datos del fichero JSON en la variable direcciones_dict que nos permitirá acceder a los diversos campos del JSON
    return (direcciones_dict)


def getClientHosts():
    with open('/Diccionarios/host.json', 'r') as f:  # Se realiza la lectura del fichero JSON
        diccionario_hosts = json.load(f)  # Se guardan los datos del fichero JSON en la variable direcciones_dict que nos permitirá acceder a los diversos campos del JSON

    hosts = diccionario_hosts.fromkeys(diccionario_hosts.keys())
    values = []
    for host in diccionario_hosts:
        if (host.get("tipo") == "Cliente" and host.get("team") == "BT"):
            values.append({'username': host.get("username"), 'password': host.get("password"), 'port': host.get("port"),
                           'name': host.get("name"), 'id': host.get("id"), 'team': host.get("team"), 'tipo': host.get("tipo"),
                           'description': host.get("description"), 'nics': host.get("nics")})
    hosts['hosts'] = values
    return (hosts)

def getServerHosts():
    with open('/Diccionarios/host.json', 'r') as f:  # Se realiza la lectura del fichero JSON
        diccionario_hosts = json.load(
            f)  # Se guardan los datos del fichero JSON en la variable direcciones_dict que nos permitirá acceder a los diversos campos del JSON

    hosts = diccionario_hosts.fromkeys(diccionario_hosts.keys())
    values = []
    for host in diccionario_hosts:
        if (host.get("tipo") == "Servidor" and host.get("team") == "BT"):
            values.append({'username': host.get("username"), 'password': host.get("password"), 'port': host.get("port"),
                           'name': host.get("name"), 'id': host.get("id"), 'team': host.get("team"),
                           'tipo': host.get("tipo"),
                           'description': host.get("description"), 'nics': host.get("nics")})
    hosts['hosts'] = values
    return (hosts)

def getAttackHosts():
    with open('/Diccionarios/host.json', 'r') as f:  # Se realiza la lectura del fichero JSON
        diccionario_hosts = json.load(
            f)  # Se guardan los datos del fichero JSON en la variable direcciones_dict que nos permitirá acceder a los diversos campos del JSON

    hosts = diccionario_hosts.fromkeys(diccionario_hosts.keys())
    values = []
    for host in diccionario_hosts:
        if (host.get("team") == "RT"):
            values.append({'username': host.get("username"), 'password': host.get("password"), 'port': host.get("port"),
                           'name': host.get("name"), 'id': host.get("id"), 'team': host.get("team"),
                           'tipo': host.get("tipo"),
                           'description': host.get("description"), 'nics': host.get("nics")})
    hosts['hosts'] = values
    return (hosts)


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


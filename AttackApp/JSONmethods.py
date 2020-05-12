import json
import re



exp = "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$";
def existKey(lista, key):
    for x in lista:
        if(x == key):
            return True

    return False

ruta_absoluta = "C:\\Users\\Aru-kun\\Documents\\TFG\\Scripts Python\\AttackApp\\Diccionarios\\"

def getDevices():
    with open(ruta_absoluta+'dispositivos.json', 'r') as f:  # Se realiza la lectura del fichero JSON
        direcciones_dict = json.load(f)  # Se guardan los datos del fichero JSON en la variable direcciones_dict que nos permitirá acceder a los diversos campos del JSON
    return (direcciones_dict)


def getHosts():
    with open(ruta_absoluta+'host.json', 'r') as f:  # Se realiza la lectura del fichero JSON
        direcciones_dict = json.load(f)  # Se guardan los datos del fichero JSON en la variable direcciones_dict que nos permitirá acceder a los diversos campos del JSON
    return (direcciones_dict)


def getClientHosts():
    with open('\\Diccionarios\\host.json', 'r') as f:  # Se realiza la lectura del fichero JSON
        diccionario_hosts = json.load(f)  # Se guardan los datos del fichero JSON en la variable direcciones_dict que nos permitirá acceder a los diversos campos del JSON

    hosts = diccionario_hosts.fromkeys(diccionario_hosts.keys())
    values = []
    for host in diccionario_hosts:
        if (host.get("tipo") == "Cliente" and host.get("team") == "BT"):
            values.append({'name': host.get("name"), 'id': host.get("id"), 'team': host.get("team"), 'tipo': host.get("tipo"), 'SO':host.get("SO"),
                           'description': host.get("description"), 'nics': host.get("nics")['data']})
    hosts['hosts'] = values
    return (hosts)

def getServerHosts():
    with open('\\Diccionarios\\host.json', 'r') as f:  # Se realiza la lectura del fichero JSON
        diccionario_hosts = json.load(
            f)  # Se guardan los datos del fichero JSON en la variable direcciones_dict que nos permitirá acceder a los diversos campos del JSON

    hosts = diccionario_hosts.fromkeys(diccionario_hosts.keys())
    values = []
    for host in diccionario_hosts:
        if (host.get("tipo") == "Servidor" and host.get("team") == "BT"):
            values.append({'username': host.get("username"), 'password': host.get("password"), 'port': host.get("port"),'name': host.get("name"), 'id': host.get("id"),
                           'team': host.get("team"), 'tipo': host.get("tipo"), 'SO':host.get("SO"),
                           'description': host.get("description"), 'nics': host.get("nics")['data']})
    hosts['hosts'] = values
    return (hosts)

def getAttackHosts():
    with open('\\Diccionarios\\host.json', 'r') as f:  # Se realiza la lectura del fichero JSON
        diccionario_hosts = json.load(
            f)  # Se guardan los datos del fichero JSON en la variable direcciones_dict que nos permitirá acceder a los diversos campos del JSON

    hosts = diccionario_hosts.fromkeys(diccionario_hosts.keys())
    values = []
    for host in diccionario_hosts:
        if (host.get("team") == "RT"):
            values.append({'name': host.get("name"), 'id': host.get("id"), 'team': host.get("team"),
                           'tipo': host.get("tipo"),
                           'description': host.get("description"), 'nics': host.get("nics")['data']})
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
            if(device.get("id")==i or device.get("id")==getDeviceByIp(i)):
                values.append({'username': device.get("username"), 'password': device.get("password"), 'port': device.get("port"), 'name': device.get("name"), 'id': device.get("id"),
     'team': device.get("team"), 'tipo': device.get("tipo"), 'SO':device.get("SO"), 'description': device.get("description"), 'nics': device.get("nics")})

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
            if(host.get("id")==i or host.get("id") == getHostByIp(i)):
                values.append({'username': host.get("username"), 'password': host.get("password"), 'port': host.get("port"), 'name': host.get("name"), 'id': host.get("id"),
     'team': host.get("team"), 'tipo': host.get("tipo"), 'SO':host.get("SO"), 'description': host.get("description"), 'nics': host.get("nics")})



    diccionario['hosts'] = values
    print("claves del diccionario: ")
    print(diccionario.keys())
    print(diccionario)
    return(diccionario)

def getClientHostsBynic(nics):
    direcciones_dict = getHosts()
    values = []

    print("He entrado en getClientHostsBynic")
    #print(direcciones_dict)
    clientes = direcciones_dict.fromkeys(direcciones_dict.keys())
    print(clientes)
    #print(nics)

    for i in nics:
        ip = re.search(exp, i)
        if (ip):
            i = getHostByIp(i)
        for cliente in direcciones_dict.get("hosts"):
            print("i = " + i)
            if(cliente.get("id")==i and cliente.get("tipo") == "Cliente"):
                print("He entrado en el IF")
                values.append({'username': cliente.get("username"), 'password': cliente.get("password"), 'port': cliente.get("port"), 'name': cliente.get("name"), 'id': cliente.get("id"),
     'team': cliente.get("team"), 'tipo': cliente.get("tipo"), 'SO':cliente.get("SO"), 'description': cliente.get("description"), 'nics': cliente.get("nics")})


    print("VALUES = ".format(values))
    clientes['hosts'] = values
    print("claves del diccionario: ")
    print(clientes.keys())
    print(clientes)
    return(clientes)


def getServerHostsBynic(nics):
    direcciones_dict = getHosts()
    values = []
    host = ""

    print("He entrado en getJsonBynic")
    print(direcciones_dict)
    servidores = direcciones_dict.fromkeys(direcciones_dict.keys())
    print(servidores)
    print(nics)

    for i in nics:
        ip = re.search(exp, i)

        if(ip):
            i = getHostByIp(i)
        for servidor in direcciones_dict.get("hosts"):
            if(servidor.get("id")==i and servidor.get("tipo") == "Servidor"):
                print("Estoy construyendo el JSON")
                values.append({'username': servidor.get("username"), 'password': servidor.get("password"), 'port': servidor.get("port"), 'name': servidor.get("name"), 'id': servidor.get("id"),
     'team': servidor.get("team"), 'tipo': servidor.get("tipo"), 'SO':servidor.get("SO"), 'description': servidor.get("description"), 'nics': servidor.get("nics")})

    servidores['hosts'] = values
    print("claves del diccionario: ")
    print(servidores.keys())
    print(servidores)
    return(servidores)

def getHostByIp(ip):
    direcciones_dict = getHosts()
    host = ""
    print("ip = " + ip)
    print("He entrado en getHostByIp")
    for ip_host in direcciones_dict.get("hosts"):
        print("ip-gestion = ", ip_host.get("nics")['management']['IP'])
        if(ip == ip_host.get("nics")['management']['IP'] or ip == ip_host.get("nics")['data']['IP']):
            print("Se comprueba la condición y es true")
            host = ip_host.get("id")

    print("El hosts es = ")
    print(host)
    return (host)


def getDeviceByIp(ip):
    direcciones_dict = getDevices()
    device = ""
    print("ip = " + ip)
    print("He entrado en getHostByIp")
    for ip_device in direcciones_dict.get("devices"):
        print("ip-gestion = ", ip_device.get("nics")['management']['IP'])
        if (ip == ip_device.get("nics")['management']['IP']):
            print("Se comprueba la condición y es true")
            device = ip_device.get("id")

    print("El hosts es = ")
    print(device)
    return (device)

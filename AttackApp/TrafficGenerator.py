from scp import SCPClient

from GUIControllerAttack import *
from sshConnection import *
from updateFile import *
import json
from os import remove


def generarTrafico(clientes_hosts, servidores_hosts, ruta_diccionario = "", ruta_trafficFlow = ""):

    #Primero, escribimos en un diccionario JSON la lista de servidores a los cuales queremos generar el tráfico
    with open('Diccionarios\\servidores_hosts.json', 'w') as file:
        json.dump(servidores_hosts, file, indent=4)

    #Ruta por defecto donde se guardará el diccionario y el archivo trafficFlow.py
    ruta_diccionario = "\Diccionarios\servidores_hosts.json"

   # if(ruta_trafficFlow == ""):
    ruta_trafficFlow = "trafficFlow.py"

    for host in clientes_hosts.get("hosts"):

        username = host.get("username")
        password = host.get('password')
        port = int(host.get('port'))
        sistema = host.get('SO')
        ip = host.get("nics")['data']['IP']
        ssh = connection(ip, port, username, password)
        # Cargamos el diccionario y el fichero trafficFlow dentro del host correspondiente
        updateFile(ssh, "TrafficFlow", ruta_diccionario, sistema, ruta_diccionario)
        updateFile(ssh, "TrafficFlow", ruta_trafficFlow, sistema, ruta_trafficFlow)
        #Eliminamos el archivo enviado a la Raspberry Pi cliente para que en la siguiente llamada no se sobreescriba el archivo
        #añadiendose más cantidad de dispositivos hosts.
        remove("Diccionarios\servidores_hosts.json")

        if(sistema == "Kali Linux"):
            stdin, stdout, stderr = ssh.exec_command(
            'python3  /root/Documents/script/trafficFlow.py')
        elif(sistema == "Ubuntu Mate"):
            stdin, stdout, stderr = ssh.exec_command(
                'python3  /home/ucase/Documentos/trafficFlow.py')
        ssh.close()
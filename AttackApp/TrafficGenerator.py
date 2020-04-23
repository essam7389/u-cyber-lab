from scp import SCPClient

from GUIControllerAttack import *
from sshConnection import *
from updateFile import *
import json


def generarTrafico(clientes_hosts, servidores_hosts, ruta_diccionario = "", ruta_trafficFlow = ""):

    #Primero, escribimos en un diccionario JSON la lista de servidores a los cuales queremos generar el tráfico
    with open('Diccionarios\servidores_hosts.json', 'w') as file:
        json.dump(servidores_hosts, file, indent=4)

    #Ruta por defecto donde se guardará el diccionario y el archivo trafficFlow.py
    if(ruta_diccionario == ""):
        ruta_diccionario = "C:\Users\Aru-kun\Documents\TFG\Scripts Python\AttackApp\Diccionarios\servidores_hosts.json"
    if(ruta_trafficFlow == ""):
        ruta_trafficFlow = "C:\Users\Aru-kun\Documents\TFG\Scripts Python\AttackApp\trafficFlow.py"

    for host in clientes_hosts.get("hosts"):

        username = host.get("username")
        password = host.get('password')
        port = int(host.get('port'))
        sistema = host.get('sistema')
        ip = host.get("nics")['management']['IP']
        ssh = connection(ip, port, username, password)
        # Cargamos el diccionario y el fichero trafficFlow dentro del host correspondiente
        updateFile(ssh, ruta_diccionario, sistema, "servidores_hosts.json")
        updateFile(ssh, ruta_trafficFlow, sistema, "trafficFlow.py")
        if(sistema == "Kali Linux"):
            stdin, stdout, stderr = ssh.exec_command(
            'python3  /root/Documents/script/trafficFlow.py')
        elif(sistema == "Ubuntu Mate"):
            stdin, stdout, stderr = ssh.exec_command(
                'python3  /home/ucase/Documentos/trafficFlow.py')
        ssh.close()
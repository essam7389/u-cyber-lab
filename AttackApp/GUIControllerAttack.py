from JSONmethods import *
from TrafficGenerator import generarTrafico
from operationsServers import *
from sshConnection import connection
from scanPorts import *
from sshAttack import *
from monitoring import *

def controller(accion, operacion, hosts_origen = [], hosts_destino = [], mask = [], tiempo = 0, suboperacion = "", GUI=None):
    '''
    :param accion: Recibo una acción que puede ser: Apagar, Reiniciar, Resetear o Consultar
    :param operacion: Recibo una operación que será "-a" (todos los dispositivos) o "-d" (1 o varios dispositivos concretos)
    :param hosts_origen: Recibo una lista vacía ("-a") o una lista con los host a los que se aplicará la acción ("-d)
    :param hosts_destino: Recibe una lista de hosts, en caso contrario la lista estará vacía.
    :param tiempo:
    :param suboperacion:
    :param GUI: Referencia a la interfáz gráfica (sólo se pasa cuando sea necesario)
    :return: Nada
    '''
    #print("dispositivos = " .format(hosts))
    #print(hosts)
    print("operación = ".format( operacion))
    #print("dispositivos = " .format(hosts))


    #Se obtienen los clientes y los servidores en función de la operación seleccionada (-a: todos los servidores y clientes; -d: servidores y clientes concretos)
    if(accion == "TrafficFlow"):
        if (operacion == "-a"):
            clientes_hosts = getClientHosts()
            servidores_hosts = getServerHosts()
        else:
            clientes_hosts = getClientHostsBynic(hosts_origen)
            servidores_hosts = getServerHosts(hosts_destino)

    elif(accion == "Scan" or accion == "SSHAttack"):
        atacantes_hosts = getHostsBynic(hosts_origen)
    elif(accion == "Servidor"):
        if(operacion == "-a"):
            servidores_hosts = getServerHosts()
        else:
            servidores_hosts = getServerHostsBynic(hosts_destino)
    else:
        if(operacion == "-a"):
            clientes_hosts = getHosts()
            servidores_hosts = getHosts()
        else:
            clientes_hosts = getHostsBynic(hosts_origen)
            servidores_hosts = getHostsBynic(hosts_destino)

    #Se realizan las llamadas a las diferentes funciones en base a la acción que se haya seleccionado
    if(accion == "TrafficFlow"):
        generarTrafico(clientes_hosts, servidores_hosts)

    elif(accion == "Servidor"):
        if(suboperacion == "-s"):
            desactivarServidor(servidores_hosts)
        else:
            print("Estoy llamando a la función")
            activarServidor(servidores_hosts)

    elif(accion == "Scan"):
        mascara = iter(mask)
        for atacante  in atacantes_hosts.get("hosts"):
            username = atacante.get("username")
            password = atacante.get("password")
            port = atacante.get("port")
            ip = atacante.get("nics")['management']['IP']
            print("IP = " + ip)
            for target in hosts_destino:
                ssh = connection(ip, port, username, password)
                resultado = scan(ssh, target, mascara)
                if(GUI.state()):
                    print() #imprimirScanGUI(resultado)
                mascara.__next__()
    elif(accion == "SSHAttack"):
        print("He entrado en la acción SSHAttack")

        for atacante in atacantes_hosts.get('hosts'):
            ip = atacante.get("nics")['management']['IP']
            username = atacante.get('username')
            password = atacante.get('password')
            puerto = atacante.get('port')
            sistema = atacante.get('SO')

            print("Intento conectar con el atacante")
            ssh = connection(ip, puerto, username, password)
            sshAttack(ssh, hosts_destino, sistema, usernarme_dict="", password_dict="")

    elif(accion == "Monitorizar"):
        monitorizar(hosts_destino)





1
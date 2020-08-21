from tkinter.ttk import Progressbar
from tkinter import *
from GUIScanDisplay import *

from JSONmethods import *
from TrafficGenerator import *
from operationsServers import *
from sshConnection import connection
from scanPorts import *
from sshAttack import *
from monitoring import *


'''def actionConfirmation(accion, operacion, hosts_origen = [], hosts_destino = [], mask = [], tiempo = 0, suboperacion = "", GUI=None, GUIsecundaria=None):
    controller(accion, operacion, hosts_origen, hosts_destino, mask, tiempo, suboperacion, GUI)
    GUIsecundaria.destroy()
    loading(GUI)'''

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
    #print("operación = ".format(operacion))
    #print("dispositivos = " .format(hosts))


    #Se obtienen los clientes y los servidores en función de la operación seleccionada (-a: todos los servidores y clientes; -d: servidores y clientes concretos)
    if(accion == "TrafficFlow"):
        if (operacion == "-a"):
            clientes_hosts = getClientHosts()
            servidores_hosts = getServerHosts()
        elif(suboperacion == "--s"):
            clientes_hosts = getClientHostsBynic(hosts_origen)
        else:
            clientes_hosts = getClientHostsBynic(hosts_origen)
            servidores_hosts = getServerHostsBynic(hosts_destino)

    elif(accion == "Scan" or accion == "SSHAttack"):
        atacantes_hosts = getHostsBynic(hosts_origen)
    elif(accion == "Servidor"):
        if(operacion == "-a"):
            servidores_hosts = getServerHosts()
        else:
            servidores_hosts = getServerHostsBynic(hosts_destino)
    else:
        if(operacion == "-a"):
            clientes_hosts = getDevices()
            servidores_hosts = getDevices()
        else:
            clientes_hosts = getDevicesBynic(hosts_origen)
            servidores_hosts = getDevicesBynic(hosts_destino)

    #Se realizan las llamadas a las diferentes funciones en base a la acción que se haya seleccionado
    if(accion == "TrafficFlow"):
        if(suboperacion == "--s"):
            apagarTrafico(clientes_hosts)
        else:
            generarTrafico(clientes_hosts, servidores_hosts, tiempo)

    elif(accion == "Servidor"):
        if(suboperacion == "--s"):
            desactivarServidor(servidores_hosts)
        else:
            #print("Estoy llamando a la función")
            activarServidor(servidores_hosts)

    elif(accion == "Scan"):
        mascara = iter(mask)
        for atacante  in atacantes_hosts.get("hosts"):
            username = atacante.get("username")
            password = atacante.get("password")
            port = atacante.get("port")
            ip = atacante.get("nics")['management']['IP']
            #print("IP = " + ip)
            for target in hosts_destino:
                ssh = connection(ip, port, username, password)
                #print("ip_objetivo = "+ target)

                resultado = scan(ssh, target, mascara.__next__(), GUI)
                print("Resultado = ")
                print(resultado)


    elif(accion == "SSHAttack"):
       # print("He entrado en la acción SSHAttack")
        display = False
        '''if(GUI!=None):
            print("He destruido la ventana y estoy creando la barra de progreso")
            loading(GUI)

        '''

        for atacante in atacantes_hosts.get('hosts'):
            ip = atacante.get("nics")['management']['IP']
            username = atacante.get('username')
            password = atacante.get('password')
            puerto = atacante.get('port')
            sistema = atacante.get('SO')

            #print("Intento conectar con el atacante")
            ssh = connection(ip, puerto, username, password)
            sshAttack(ssh, hosts_destino, sistema, usernarme_dict="", password_dict="", GUI=GUI)

        #loadingStop(GUI)

    elif(accion == "Monitorizar"):
        monitorizar(clientes_hosts, servidores_hosts)


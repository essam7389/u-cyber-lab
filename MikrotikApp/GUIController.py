from MikrotikApp.Reset import reset
from MikrotikApp.estado import *
from MikrotikApp.reboot import reboot
from MikrotikApp.shutdown import apagar
from MikrotikApp.sshConnection import connection
from MikrotikApp.GUIconsultaDisplay import imprimirEstadoGUI
from MikrotikApp.JSONmethods import *
from MikrotikApp.shutdownHost import *
from MikrotikApp.rebootHost import *

def controller(accion, operacion, dispositivos = [], GUI=None, rutas = []):
    '''
    :param accion: Recibo una acción que puede ser: Apagar, Reiniciar, Resetear o Consultar
    :param operacion: Recibo una operación que será "-a" (todos los dispositivos) o "-d" (1 o varios dispositivos concretos)
    :param dispositivos: Recibo una lista vacía ("-a") o una lista con los dispositivos a los que se aplicará la acción ("-d)
    :param hosts: Recibe una lista de hosts, en caso contrario la lista estará vacía.
    :param GUI: Referencia a la interfáz gráfica (sólo se pasa cuando sea necesario)
    :param rutas: Recibo una lista de rutas que contendrá las rutas de cada uno de los ficheros de backup (sólo se ussa cuando se selecciona la opción Resetear)
    :return: Nada
    '''
    print("dispositivos = " .format(dispositivos))
    print(dispositivos)
    print("operación = ".format( operacion))
    print("dispositivos = " .format(dispositivos))
    if(operacion == "-a"):
        diccionario = getDevices()
        diccionario_hosts = getHosts()

    else:
        diccionario = getDevicesBynic(dispositivos)
        diccionario_hosts = getHostsBynic(dispositivos)
        '''
         print("Error, los ids insertados no son válidos")
        print("Cancelando...")
        exit()
        '''

    print("diccionario = ".format(diccionario))
    if(accion == "Apagar"):
        for direccion in diccionario.get("devices"):
            username = direccion.get("username")
            password = direccion.get('password')
            port = int(direccion.get('port'))
            print()
            ip = direccion.get("nics")['management']['IP']
            ssh = connection(ip, port, username, password)
            apagar(ssh)
            ssh.close()

        for host in diccionario_hosts.get("hosts"):
            # Ahora van los host
            username = host.get("username")
            password = host.get('password')
            port = int(host.get('port'))
            print()
            ip = host.get("nics")['management']['IP']
            ssh = connection(ip, port, username, password)
            apagarHost(ssh)
            ssh.close()



    elif(accion == "Reiniciar"):
        for direccion in diccionario.get("devices"):
            print("He entrado en reiniciar")
            username = direccion.get("username")
            password = direccion.get('password')
            port = int(direccion.get('port'))
            ip = direccion.get("nics")['management']['IP']
            ssh = connection(ip, port, username, password)
            reboot(ssh)
            ssh.close()

        for host in diccionario_hosts.get("hosts"):
            # Ahora van los host
            username = host.get("username")
            password = host.get('password')
            port = int(host.get('port'))
            print()
            ip = host.get("nics")['management']['IP']
            ssh = connection(ip, port, username, password)
            reiniciarHost(ssh)
            ssh.close()

    elif(accion == "Resetear" and rutas != []):
        i = 0
        for direccion in diccionario.get("devices"):
            username = direccion.get("username")
            password = direccion.get('password')
            port = int(direccion.get('port'))
            ip = direccion.get("nics")['management']['IP']
            ssh = connection(ip, port, username, password)
            print("LA RUTA ES= ")
            print(rutas[i].name)
            reset(ssh, rutas[i].name)
            ssh.close()
            i += 1

    else:
        names = []
        response_gestion = []
        response_datos = []
        ips_gestion = []
        ips_datos = []


        for direccion in diccionario.get("devices"):
            ip_gestion = "0.0.0.0"
            ip_datos = "0.0.0.0"
            print("name = " + direccion["name"])
            if(existKey(direccion.get("nics").keys(), "management")):
                ip_gestion = direccion.get("nics")['management']['IP']

            if (existKey(direccion.get("nics").keys(), "data")):
                ip_datos = direccion.get("nics")['data']['IP']

            respuesta = estado(ip_gestion, ip_datos)

            names.append(direccion["name"])

            ips_gestion.append(ip_gestion)
            ips_datos.append(ip_datos)
            response_gestion.append(respuesta[0])
            response_datos.append(respuesta[1])

        for direccion in diccionario_hosts.get("hosts"):
            ip_gestion = "0.0.0.0"
            ip_datos = "0.0.0.0"
            print("name = " + direccion["name"])
            if(existKey(direccion.get("nics").keys(), "management")):
                ip_gestion = direccion.get("nics")['management']['IP']

            if (existKey(direccion.get("nics").keys(), "data")):
                ip_datos = direccion.get("nics")['data']['IP']

            respuesta = estado(ip_gestion, ip_datos)

            names.append(direccion["name"])

            ips_gestion.append(ip_gestion)
            ips_datos.append(ip_datos)
            response_gestion.append(respuesta[0])
            response_datos.append(respuesta[1])


        print("El estado de la interfáz gráfica es = ")
        if(GUI.state()):
            imprimirEstadoGUI(GUI, names, response_gestion, response_datos, ips_gestion, ips_datos)
        else:
            imprimirEstado(names, response_gestion, response_datos, ips_gestion, ips_datos)


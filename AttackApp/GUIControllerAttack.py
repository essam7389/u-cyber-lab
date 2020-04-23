from JSONmethods import *
from TrafficGenerator import generarTrafico
from sshConnection import connection

def controller(accion, operacion, hosts_origen = [], hosts_destino = [], GUI=None):
    '''
    :param accion: Recibo una acción que puede ser: Apagar, Reiniciar, Resetear o Consultar
    :param operacion: Recibo una operación que será "-a" (todos los dispositivos) o "-d" (1 o varios dispositivos concretos)
    :param dispositivos: Recibo una lista vacía ("-a") o una lista con los dispositivos a los que se aplicará la acción ("-d)
    :param hosts: Recibe una lista de hosts, en caso contrario la lista estará vacía.
    :param GUI: Referencia a la interfáz gráfica (sólo se pasa cuando sea necesario)
    :param rutas: Recibo una lista de rutas que contendrá las rutas de cada uno de los ficheros de backup (sólo se ussa cuando se selecciona la opción Resetear)
    :return: Nada
    '''
    #print("dispositivos = " .format(hosts))
    #print(hosts)
    print("operación = ".format( operacion))
    #print("dispositivos = " .format(hosts))

    #Se obtienen los clientes y los servidores en función de la operación seleccionada (-a: todos los servidores y clientes; -d: servidores y clientes concretos)
    if (operacion == "-a"):
        clientes_hosts = getClientHosts()
        servidores_hosts = getServerHosts()

    else:
        clientes_hosts = getDevicesBynic(hosts_origen)
        servidores_hosts = getDevicesBynic(hosts_destino)


    if(accion == "TrafficFlow"):
        generarTrafico(clientes_hosts, servidores_hosts)




    elif(accion == "Servidor"):
        print()





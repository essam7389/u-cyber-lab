import subprocess

def estado(ip_gestion, ip_datos):
    print("Ha continuación se mostrarán las conexiones activas entre este ordenador y el resto de dispositivos.")

    cont = 0
    response = []

    if(ip_gestion!="0.0.0.0"):
        p = subprocess.Popen(['ping', '-n', '3', '-w', '2', ip_gestion])
        p.wait()
        if p.poll() == 0:
            response.append(0)
        else:
            response.append(1)
    else:
        response.append(1)

    if(ip_datos!="0.0.0.0"):
        p = subprocess.Popen(['ping', '-n', '3', '-w', '2', ip_datos])
        p.wait()

        if p.poll() == 0:
            response.append(0)
        else:
            response.append(1)
    else:
        response.append(1)

    return response


def imprimirEstado(names, response_gestion, response_datos, ips_gestion, ips_datos):

    print("############################################################################################ \n")

    print("Las direcciones de la RED DE GESTIÓN disponibles son: ")

    print("")

    print(" Nombre      |        IP        |       Estado      ")
    print("----------------------------------------------------")
    print("")

    cont = 0;
    i = 0
    y  = response_gestion

    print("names = " + names[cont])

    for x in ips_gestion:
        if(x!="0.0.0.0" and y[i] == 0):
            ip = x
            print(names[cont] + "         " + ip + "        ACTIVO")
        elif(x!="0.0.0.0"):
            ip = x
            print(names[cont] + "         " + ip + "        INACTIVO")
        i += 1
        cont += 1

    print("")

    print("---------------------------------------------------------------------------------------------")

    print("")

    print("Las direcciones de la RED DE DATOS disponibles son: \n")


    print(" Nombre      |        IP        |       Estado      ")
    print("----------------------------------------------------")

    print("")

    cont = 0
    i = 0
    y = response_datos
    for x in ips_datos:
        if (x!="0.0.0.0" and y[i] == 0):
            ip = x
            print(names[cont] + "         " + ip + "        ACTIVO")
        elif(x!="0.0.0.0"):
            ip = x
            print(names[cont] + "         " + ip + "        INACTIVO")

        i += 1
        cont += 1
    print("")
    print("############################################################################################ \n")


   # print(response[cont])


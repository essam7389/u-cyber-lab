import tiempo

def apagar(ssh):
    tm = tiempo.tiempo()  # Calculamos el tiempo pasado en segundos desde el año 1970
    result = tiempo.localtime(
        tm + 60)  # Se suma a ese tiempo "tm" calculado el tiempo en el cual queremos que nuestro dispositivo se reinicie
    print("Son las:")
    print(tiempo.strftime('%H:%M:%S'))  # Hora actual

    print("El dispositivo se reiniciará a las: ")
    time_string = tiempo.strftime("%H:%M:%S", result)
    print(time_string)  # Hora en la cual el dispositivo se reiniciará
    stdin, stdout1, stderr = ssh.exec_command(
        '/system script remove [/system script find]')  # Elimina todos los scripts
    stdin, stdout2, stderr = ssh.exec_command(
        '/system scheduler remove [/system scheduler find]')  # Elimina todos los planificadores del dispositivo
    stdout = stdout2.readlines()
    print(stdout)
    print(time_string)
    stdin, stdout3, stderr = ssh.exec_command('/system script add name="apagado" source="/system reboot"')  #
    stdin, stdout4, stderr = ssh.exec_command(
        '/system scheduler add name=apagado start-time=' + time_string + ' on-event=apagado')  #
    stdout = stdout4.readlines()
    print(stdout)
    print("Apagando...")
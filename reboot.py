from tiempo import tiempo

def reboot(ssh):
    #tm = time.time() #Calculamos el tiempo pasado en segundos desde el año 1970
    #result = time.localtime(tm+60) #Se suma a ese tiempo "tm" calculado el tiempo en el cual queremos que nuestro dispositivo se reinicie
    #print("Son las:")
    #print (time.strftime('%H:%M:%S')) #Hora actual

    print("El dispositivo se reiniciará a las: ")
    time_string = tiempo()
    print(time_string) #Hora en la cual el dispositivo se reiniciará
    stdin, stdout1, stderr = ssh.exec_command('/system script remove [/system script find]') #Elimina todos los scripts
    stdin, stdout2, stderr = ssh.exec_command('/system scheduler remove [/system scheduler find]') #Elimina todos los planificadores del dispositivo
    stdout = stdout2.readlines()
    print(stdout)
    print(time_string)
    stdin, stdout3, stderr = ssh.exec_command('/system script add name="reinicio" source="/system reboot"') #
    stdin, stdout4, stderr = ssh.exec_command('/system scheduler add name=reinicio start-time='+time_string+' on-event=reinicio') #
    stdout = stdout4.readlines()
    #print('/system scheduler add name=reinicio start-time='+time_string+'on-event=reinicio')
    print(stdout)
    print("Reiniciando...")
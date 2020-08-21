from tiempo import tiempo

def apagar(ssh):
    '''
      :param ssh: Recibe una conexión SSH al o los dispositivos que se desean apagar.
      :return: No devuelve nada
      '''
    print("El dispositivo se apagará a las: ")
    time_string = tiempo(ssh)
    print(time_string)  # Hora en la cual el dispositivo se apagará
    stdin1, stdout1, stderr1 = ssh.exec_command(
        '/system script remove [/system script find]')  # Elimina todos los scripts
    stdin2, stdout2, stderr2 = ssh.exec_command(
        '/system scheduler remove [/system scheduler find]')  # Elimina todos los planificadores del dispositivo
    stdout = stdout2.readlines()
    print(stdout)
    print(time_string)
    stdin3, stdout3, stderr3 = ssh.exec_command('/system script add name="apagado" source="/system shutdown"')  #
    stdin4, stdout4, stderr4 = ssh.exec_command(
        '/system scheduler add name=apagado start-time=' + time_string + ' on-event=apagado')  #
    stdout = stdout4.readlines()
    print(stdout)
    print("Apagando...")
    ssh.close()
    
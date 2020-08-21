import sshConnection

def reiniciarHost(ssh):
    '''
        :param ssh: Recibe una conexión SSH al o los host que se desean reiniciar.
        :return:
    '''
    print("El host se reiniciará en 1 minuto: ")

    stdin, stdout, stderr = ssh.exec_command('sudo reboot')  #
    stdout = stdout.readlines()
    print(stdout)
    print("Reiniciando...")
    ssh.close()



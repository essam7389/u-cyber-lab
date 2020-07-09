

def apagarHost(ssh):
    '''
    :param ssh: Recibe una conexión SSH al o los host que se desean apagar.
    :return:
    '''
    print("El host se apagará en 1 minuto: ")

    stdin, stdout, stderr = ssh.exec_command('sudo shutdown')  #
    stdout = stdout.readlines()
    print(stdout)
    print("Apagando...")

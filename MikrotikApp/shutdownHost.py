

def apagarHost(ssh):

    print("El host se apagará en 1 minuto: ")

    stdin, stdout, stderr = ssh.exec_command('sudo shutdown')  #
    stdout = stdout.readlines()
    print(stdout)
    print("Apagando...")

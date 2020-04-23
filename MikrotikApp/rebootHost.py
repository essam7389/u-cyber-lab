import sshConnection

def reiniciarHost(ssh):

    print("El host se reiniciará en 1 minuto: ")

    stdin, stdout, stderr = ssh.exec_command('sudo reboot')  #
    stdout = stdout.readlines()
    print(stdout)
    print("Reiniciando...")



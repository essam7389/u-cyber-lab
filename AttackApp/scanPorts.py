from sshConnection import *

def scan(ssh, ip, mascara):
    stdin, stdout, stderr = ssh.exec_command("nmap "+ ip)
    for line in stdout:
        salida = "'... '" + line.strip('\n')

    print(salida)
    ssh.close()
    return(salida)
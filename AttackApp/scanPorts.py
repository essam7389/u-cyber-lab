from sshConnection import *

def scan(ssh, ip, mascara):
    stdin, stdout, stderr = ssh.exec_command("nmap "+ ip +"/"+mascara)
    respuesta = ""
    for line in stdout:
        salida = "'... '" + line.strip('\n')
        respuesta += salida
        print(salida)


    ssh.close()
    return(respuesta)
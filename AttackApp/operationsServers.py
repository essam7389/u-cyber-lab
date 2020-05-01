from sshConnection import *

def activarServidor(servidores_hosts):
    print("He entrado en activar servidor")

    for servidor in servidores_hosts.get("hosts"):
        print(servidor)
        username = servidor.get("username")
        password = servidor.get("password")
        puerto = servidor.get("port")
        ip = servidor.get("nics")['management']['IP']
        ssh = connection(ip, puerto, username, password)
        stdin, stdout, stderr = ssh.exec_command("echo "+ password + " | sudo -S systemctl start apache2")
        for line in stdout:
            print('... ' + line.strip('\n'))

        ssh.close()



def desactivarServidor(servidores_hosts):
    for servidor in servidores_hosts.get("hosts"):
        username = servidor.get("username")
        password = servidor.get("password")
        puerto = servidor.get("port")
        ip = servidor.get("nics")['management']['IP']
        ssh = connection(ip, puerto, username, password)
        stdin, stdout, stderr = ssh.exec_command("echo " + password + " | sudo -S systemctl stop apache2")
        for line in stdout:
            print('... ' + line.strip('\n'))

        ssh.close()
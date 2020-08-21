from sshConnection import *

def activarServidor(servidores_hosts):
    #print("He entrado en activar servidor")

    for servidor in servidores_hosts.get("hosts"):
        print(servidor)
        username = servidor.get("username")
        password = servidor.get("password")
        puerto = servidor.get("port")
        ip_gestion = servidor.get("nics")['management']['IP']
        ip_datos = servidor.get("nics")['data']['IP']
        ssh = connection(ip_gestion, puerto, username, password)
        print("Activando servidor apache...")
        stdin, stdout, stderr = ssh.exec_command("echo "+ password + " | sudo -S systemctl start apache2")
        for line in stdout:
            print('... ' + line.strip('\n'))

        print("Activando servidor Web...")

        stdin, stdout, stderr = ssh.exec_command("cd /var/www/salonmangamadrid_final/bin && php console server:start " + ip_datos + ":8000")
        print("He terminado la activación del servidor")

        ssh.close()



def desactivarServidor(servidores_hosts):
    for servidor in servidores_hosts.get("hosts"):
        username = servidor.get("username")
        password = servidor.get("password")
        puerto = servidor.get("port")
        ip = servidor.get("nics")['management']['IP']
        ssh = connection(ip, puerto, username, password)
        print("Desactivando servidor apache...")
        stdin, stdout, stderr = ssh.exec_command("echo " + password + " | sudo -S systemctl stop apache2")
        for line in stdout:
            print('... ' + line.strip('\n'))

        print("Desactivando servidor Web...")

        stdin, stdout, stderr = ssh.exec_command(
            "php console server:stop | cd /var/www/salonmangamadrid_final/bin")
        for line in stdout:
            print('... ' + line.strip('\n'))

    ssh.close()


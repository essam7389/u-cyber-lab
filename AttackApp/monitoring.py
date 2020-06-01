from sshConnection import connection


def monitorizar(hosts_emisor, hosts_receptor):
    print("He entrado en monitorizar")
    for emisor in hosts_emisor.get("devices"):
        username = emisor.get("username")
        password = emisor.get('password')
        port = int(emisor.get('port'))
        #Se obtiene la ip del diccionario de devices o de hosts para el emisor?/ Actualmente falta por filtrar la ip emisora y generar el JSON emisor que no está hecho, únicamente se recibe la ip y ya
        ip_emisor = emisor.get("nics")['management']['IP']
        print("ip_emisor = " + ip_emisor)
        ssh = connection(ip_emisor, port, username, password)
        print("Monitoraizando tráfico...")
        stdin, stdout, stderr = ssh.exec_command('/ip traffic-flow set enabled=yes')
        for target in hosts_receptor.get("devices"):
            ip_receptor = target.get("nics")['management']['IP']
            stdin, stdout, stderr = ssh.exec_command('/ip traffic-flow target add dst-address=' + ip_receptor + " port = 2055 version=9")

        respuesta = ""
        for line in stdout:
            salida = "'... '" + line.strip('\n')
            respuesta += salida
            print(salida)
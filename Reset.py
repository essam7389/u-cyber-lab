from scp import SCPClient
import  os
import tiempo

def reset(ssh, host, port, username, password):

    print (" Seleccione una carpeta de la lista: ")
    dir = "C:\\Users\Aru-kun\Documents\TFG\Backups";
    print(os.listdir(dir))

    print("Por favor introduzca el nombre de la carpeta a la cuál desea acceder")

    carpeta = input();
    dir = dir+carpeta;

    print(" Introduzca el nombre del backup que quiera cargar, tenga en cuenta que si carga un backup de manera equivocada en un dispositivo "
          "puede tener consecuencias desconocidas.: ")
    print(os.listdir(dir));

    backup = input();

    print("El backup seleccionado es= " + backup)
    print("¿Está seguro que desea cargar dicho Backup? y/n")

    confirmacion = input()

    if(confirmacion == "n"):
        print("Cancelando...")
        ssh.close()
        exit()

    print("Cargando archivo en el dispositivo seleccionado...");

    ssh.connect(host, port, username, password)
    scp = SCPClient(ssh.get_transport())
    scp.put(dir+'\\'+ backup,  remote_path=backup);

    #Send SCP command to upload backup file
   # file = "03-03-2020-Definitivo-Switch";
   # scp.put(backup, recursive=true, remote_path=host);

    print("Archivo cargado en el dispositivo");

    # Send the command (non-blocking)
    #stdin, stdout, stderr = ssh.exec_command(['/system backup load name='+backup]) #Se carga el backup.cfg y se reinstala la configuración inicial del dispositivo mikrotik

    stdin, stdout, stderr = ssh.exec_command('/system script add name="reinicio" source="/system reboot"')
    stdin, stdout, stderr = ssh.exec_command('/system scheduler add name=reinicio start-time=' + tiempo(ssh) + ' on-event=reinicio')


    ssh.close()



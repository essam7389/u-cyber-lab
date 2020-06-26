from scp import SCPClient

from tiempo import *


def reset(ssh, backup):
    scp = SCPClient(ssh.get_transport())
    scp.put(backup,  remote_path='backup');

    # Send the command (non-blocking)


    print("Archivo cargado en el dispositivo");
    time_string = tiempo(ssh)
    print(time_string)  # Hora en la cual el dispositivo se reiniciará
    stdin, stdout1, stderr = ssh.exec_command(
        '/system script remove [/system script find]')  # Elimina todos los scripts
    stdin, stdout2, stderr = ssh.exec_command(
        '/system scheduler remove [/system scheduler find]')  # Elimina todos los planificadores del dispositivo
    stdout = stdout2.readlines()
    print(stdout)
    print(time_string)

    stdin, stdout, stderr = ssh.exec_command('/system script add name="reset" source="/system reset-configuration keep-users=yes no-defaults=yes run-after-reset=backup.rsc"')
    stdin, stdout, stderr = ssh.exec_command('/system scheduler add name=reseteo start-time=' + time_string + ' on-event=reset')

    ssh.close()

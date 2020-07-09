import time
def tiempo(ssh):
    '''
    :param ssh: Recibe una conexión sshr
    :return: Devuelve el tiempo en formato horas:minutor:segundos como resultado de la operación
    '''
    tm = time.time()  # Calculamos el tiempo pasado en segundos desde el año 1970
    stdin, stdout1, stderr = ssh.exec_command('/system clock set time=' + time.strftime('%H:%M:%S'))
    stdin, stdout2, stderr = ssh.exec_command('/system clock set print')
    result = time.localtime(
        tm + 60)  # Se suma a ese tiempo "tm" calculado el tiempo en el cual queremos que nuestro dispositivo tarde en realizar la acción
    print("Son las:")
    print(time.strftime('%H:%M:%S'))  # Hora actual

    return (time.strftime("%H:%M:%S", result))

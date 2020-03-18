import time
def tiempo():
    tm = time.time()  # Calculamos el tiempo pasado en segundos desde el año 1970
    result = time.localtime(
        tm + 60)  # Se suma a ese tiempo "tm" calculado el tiempo en el cual queremos que nuestro dispositivo se reinicie
    print("Son las:")
    print(time.strftime('%H:%M:%S'))  # Hora actual

    print("El dispositivo se reiniciará a las: ")
    return (time.strftime("%H:%M:%S", result))